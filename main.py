import pygame, os, sys, pprint
from pygame.locals import *
from decimal import *
from screen import FixedScreen
from colors import Colors
from dispNotes import DispNotes
from field import Field
import convertToMap
import readMap

pygame.init() 

"""
スクリーン設定
"""
# 画面サイズ
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('C:/Windows/Fonts/Yu Gothic UI', 30)

pygame.display.set_caption('ONShooter')

"""
操作設定
"""
# 楽曲設定
MAPNAME = 'score1'
AUDIO = 'scores/' + MAPNAME + '/audio.mp3'
# ハイスピード設定
speed = 0.8
# キーコンフィグ
keyR = [pygame.K_s, pygame.K_j]
keyG = [pygame.K_d, pygame.K_k]
keyB = [pygame.K_f, pygame.K_l]

# 判定ライン・判定幅
judge_point = 600

# ノーツの大きさ
note_sizex = 98
note_sizey = 20

# 譜面データの読み込み
MAPLINK = 'scores/' + MAPNAME + '/' + MAPNAME + '.txt'
MAP = convertToMap.convertToMap(MAPLINK, Decimal(speed), judge_point, note_sizex, note_sizey)
# 譜面データから譜面本体(ノーツデータ)を書き出す
SCORE = readMap.readMap(MAP['score'])
# pprint.pprint(MAP)
# sys.exit()

# 初期画面(キー入力があった場合ゲーム本体へ遷移)
press_anykey = False
while not press_anykey:
    text = font.render('ONShooter Press any Key', False, Colors.WHITE)
    screen.blit(text, (20, 40))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            press_anykey = True
    pygame.display.update()

SCREEN = Field()
SCREEN.setData(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN.draw(screen)
pygame.display.update()
pygame.time.wait(2000)
sys.exit()
SCREEN = FixedScreen()
running = True
outNote = True
point = 0
st_time = pygame.time.get_ticks()
disp_notes = []
offset = next(iter(SCORE))
notes = SCORE.pop(offset)
# ゲームの起動
if os.path.isfile(AUDIO):
    pygame.mixer.init()
    pygame.mixer.music.load(AUDIO)
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.2)
while running:
    SCREEN.draw(screen, judge_point + 20, SCREEN_WIDTH, SCREEN_HEIGHT, 98)

    pass_time = pygame.time.get_ticks()
    nowtime = pass_time - st_time

    tl = font.render('title: ' + MAPNAME, False, Colors.WHITE)
    screen.blit(tl, (20, 40))
    pt = font.render('score: ' + str(point), False, Colors.WHITE)
    screen.blit(pt, (20, 60))
    nt = font.render('time: ' + str(round(nowtime / 1000, 2)), False, Colors.WHITE)
    screen.blit(nt, (20, 80))

    # ノーツのオフセットが経過時間になったら該当ノーツを表示キューに挿入
    if outNote and nowtime >= offset:
        for note in notes:
            note['st_time'] = nowtime
            disp_notes.append(note)

        if SCORE:
            offset = next(iter(SCORE))
            notes = SCORE.pop(offset)
        else:
            outNote = False

    # ノーツの表示と移動
    if disp_notes:
        for i, note in enumerate(disp_notes):
            dn = DispNotes(note['note'], note['x'], note['y'])
            dn.draw(screen)
            note['y'] = round((nowtime - note['st_time']) * Decimal(speed))

            if note['y'] > judge_point + 100:
                del disp_notes[i]

    for event in pygame.event.get():
        if event.type == QUIT:
            if os.path.isfile(AUDIO):
                pygame.mixer.music.stop()
            running = False
        # キーが押された際の処理
        if event.type == pygame.KEYDOWN and disp_notes:
            for i, note in enumerate(disp_notes):
                if  ((event.key in keyR and note['note_type'] == 'red') or
                    (event.key in keyG and note['note_type'] == 'green') or 
                    (event.key in keyB and note['note_type'] == 'blue')):
                    if judge_point - 100 <= note['y'] and note['y'] <= judge_point + 100:
                        point += 1
                        if judge_point - 66 <= note['y'] and note['y'] <= judge_point + 66:
                            point += 1
                        if judge_point - 33 <= note['y'] and note['y'] <= judge_point + 33:
                            point += 1   
                        dn.remove()
                        del disp_notes[i]
                        break

    pygame.display.update()            
