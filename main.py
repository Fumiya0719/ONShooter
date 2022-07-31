import pygame, sys, random, math, time, pprint
from pygame.locals import *
from decimal import *
from screen import FixedScreen
from colors import Colors
from notes import Notes
from dispNotes import DispNotes
import convertToMap
import readMap

pygame.init() 

"""
スクリーン設定
"""
# 画面サイズ
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('C:/Windows/Fonts/Yu Gothic UI', 30)

pygame.display.set_caption('ONShooter')

"""
操作設定
"""
# ハイスピード設定
speed = 1
# キーコンフィグ
keyR = [pygame.K_s, pygame.K_j]
keyG = [pygame.K_d, pygame.K_k]
keyB = [pygame.K_f, pygame.K_l]

# 判定ライン・判定幅
judge_point = 600
JUDGE_PF = 33.33
JUDGE_GR = 66.66
JUDGE_OK = 100

# 譜面データの読み込み
MAP = convertToMap.convertToMap('scores/score1.txt')
# 譜面データから譜面本体(ノーツデータ)を書き出す
SCORE = readMap.readMap(MAP['score'])
# print(SCORE)
# sys.exit()

SCREEN = FixedScreen()
running = True
outNote = True
st_time = pygame.time.get_ticks()
disp_notes = []
offset = next(iter(SCORE))
notes = SCORE.pop(offset)
# ゲームの起動
while running:
    SCREEN.draw(screen, judge_point + 20, SCREEN_HEIGHT)

    pass_time = pygame.time.get_ticks()
    nowtime = pass_time - st_time

    nt = font.render('time: ' + str(nowtime), False, Colors.WHITE)
    screen.blit(nt, (20, 60))

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
            if note['y'] == judge_point:
                print(nowtime)    

            dn = DispNotes(note['note'], note['x'], note['y'])
            dn.draw(screen)
            note['y'] = nowtime - note['st_time']

            if note['y'] > SCREEN_HEIGHT:
                del disp_notes[i]

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # キーが押された際の処理
        if event.type == pygame.KEYDOWN:
            if event.key in keyR:
                break
            if event.key in keyG:
                break
            if event.key in keyB:
                break

    pygame.display.update() 


            
