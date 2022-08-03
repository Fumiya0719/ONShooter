import pygame
from pygame.locals import *
from decimal import *
import sys, pprint

def convertToMap(mapdata, speed, judge_point, screen_width, screen_height):
    MAP = {}

    title = mapdata['title']
    bpm = Decimal(mapdata['bpm'])
    start = mapdata['offset']

    MAP['title'] = title
    MAP['bpm'] = bpm
    MAP['score'] = []

    # ノーツの大きさ

    # 譜面データをノーツデータに変換
    timing = 0
    for data in mapdata['map']:

        # BPMの更新
        if 'bpm' in data:
            bpm = data['bpm']
        # ノーツの間隔
        noteInterval = data['beat']
        # 1ビートの間隔(ms)
        beat = Decimal(60 * 1000 / bpm) / Decimal(noteInterval / 4) 

        # リスト化したデータが空だった場合、次の小節へ
        if not data['notes_list']:
            beat = Decimal(60 * 1000 / bpm) * 4
            timing += beat
        # ノーツ一覧を取得
        for j, notes in enumerate(data['notes_list']):
            # ノーツの追加処理
            # note_xo = 290
            for note in notes:
                note_obj = {}
                # 画像ファイル名の作成
                file = note[0] + '.png'
                # ノーツ画像の読み込み
                note_img = pygame.image.load('images/' + file)
                # ノーツ画像のリサイズ

                # オフセット
                offset = (timing + beat * j) + (Decimal(judge_point) / speed) + start
                offset = round(offset)

                # ノーツの生成
                note_obj['note_type'] = note[0]
                note_obj['note'] = note_img
                note_obj['offset'] = offset
                note_obj['x'] = note[1] if len(note) > 1 else False
                note_obj['y'] = False
                note_obj['ln'] = note[2] if len(note) > 2 else False
                note_obj['ex'] = note[3] if len(note) > 3 else False                

                MAP['score'].append(note_obj)
           
    return MAP
