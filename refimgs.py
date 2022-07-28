import os
# ランダム: 画像ファイル保存時の名前生成
import random, string
# タイマー: 同時複数リクエストを制限
import time
# 日付: いつまでのブックマークを取得するか
import datetime
# pixivpy: pixivからデータを抽出するAPI
from pixivpy3 import *

# import APIkey
import apikey_pi
# import Configurable
import config

USER_ID = config.USER_ID
DL_PATH = config.DL_PATH
SAVE_FOLDER = config.SAVE_FOLDER 
IMAGES_FROM = config.IMAGES_FROM
SERIAL_NUMBER = config.SERIAL_NUMBER
USING_ID = config.USING_ID
SUSPENDING_ID = config.SUSPENDING_ID
USING_TERM = config.USING_TERM
ST_TIME = config.ST_TIME
ST_SUSPENDING = config.ST_SUSPENDING
ED_TIME = config.ED_TIME
ED_SUSPENDING = config.ED_SUSPENDING
USING_COUNTER = config.USING_COUNTER
INCLUDE_TAGS = config.INCLUDE_TAGS
TAGS_LIST = config.TAGS_LIST
counter = config.counter

# Auth接続
aapi = AppPixivAPI()
aapi.auth(refresh_token = apikey_pi.REFRESH_TOKEN)

# 画像のリンクを保管する配列
illusts = []

# ブックマークを取得

if IMAGES_FROM == "bookmark":
    images_info = aapi.user_bookmarks_illust(USER_ID, 'public')
else:
    images_info = aapi.user_illusts(IMAGES_FROM)

# 画像をurl配列に挿入
is_continue_refers = True
while is_continue_refers:

    for i, b in enumerate(images_info['illusts']):

        # カウンタをセットしている場合の処理
        if USING_COUNTER:
            counter -= 1

        # ブックマーク解除基準
        # ページのブックマーク数が30未満の場合,現在のループで最後にする
        if len(images_info['illusts']) < 30:
            is_continue_refers = False

        # 次のブックマーク列の作成
        if i == 29:
            next_url = images_info['next_url']
            next_qs = aapi.parse_qs(next_url)
            if IMAGES_FROM == "bookmark":
                images_info = aapi.user_bookmarks_illust(**next_qs)
            else:
                images_info = aapi.user_illusts(**next_qs)

        # 取得した画像が指定されたIDの場合、直ちにループを終了
        if USING_ID and b['id'] == SUSPENDING_ID:
            is_continue_refers = False
            break

        # 投稿日時のフォーマット
        created_at = str(b['create_date']).split('+')[0].replace('T', ' ')
        # 期間指定あり・取得された投稿日時が開始日以前の場合,直ちにループを終了
        if USING_TERM and ST_TIME != False and b['create_date'] < ST_TIME:
            if ST_SUSPENDING:
                is_continue_refers = False
                break
            else:
                continue

        # 期間指定あり・取得された投稿日時が終了日以後の場合,画像取得をしない
        if USING_TERM and ED_TIME != False and b['create_date'] > ED_TIME:
            if ED_SUSPENDING:
                is_continue_refers = False
                break
            else:
                continue

        # タグが含まれているかどうか
        if INCLUDE_TAGS:
            illust_tags_list = []
            for tag in b['tags']:
                illust_tags_list.append(tag['name'])
            # print(illust_tags_list)
            if len(list(set(TAGS_LIST) & set(illust_tags_list))) == 0 and TAGS_LIST != []:
                continue
        
        # カウンタあり・カウンタが0になった場合,直ちにループを終了
        if USING_COUNTER and counter < 0:
            is_continue_refers = False
            break
        
        # 画像の挿入
        # 画像が1枚の場合
        if len(b['meta_pages']) == 0:
            # queue['images'].append(b['image_urls']['large'])
            illusts.append(b['meta_single_page']['original_image_url'])
        # 画像が複数枚の場合
        else:
            for m in b['meta_pages']:
                # queue['images'].append(m['image_urls']['original'])      
                illusts.append(m['image_urls']['original'])

print('Found ' + str(len(illusts)) + ' images.')

# ランダム文字列の生成
def randSTR(num):
    rands = [random.choice(string.ascii_letters + string.digits) for i in range(num)]
    return ''.join(rands)

# 保存先のパス
SAVE_PATH = DL_PATH + '/' + SAVE_FOLDER

time.sleep(2)
# ダウンロード処理
dl_count = 0
for illust in illusts:
    dl_count += 1
    # 指定されたフォルダが存在しない場合新規作成
    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    # ファイル名の設定
    file_name = str(dl_count) if SERIAL_NUMBER else randSTR(12) + '.jpg' 
    # ダウンロード処理
    aapi.download(illust, path = SAVE_PATH, name = file_name)
    print('Downloading... count: ' + str(dl_count))
    time.sleep(1)
print('Downloading: Done')
