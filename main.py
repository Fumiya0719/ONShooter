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
keyR = [pygame.K_s, pygame.K_j]
keyG = [pygame.K_d, pygame.K_k]
keyB = [pygame.K_f, pygame.K_l]

# 譜面データの読み込み
MAP = convertToMap.convertToMap('scores/score1.txt')
# 譜面データから譜面本体(ノーツデータ)を書き出す
SCORE = readMap.readMap(MAP['score'])

# 判定ライン
judge_point = 600
SCREEN = FixedScreen()

running = True
outNote = True
disp_notes = []
st_time = Decimal(time.perf_counter()).quantize(Decimal('1.0000'))
# ゲームの起動
while running:
    SCREEN.draw(screen, judge_point + 20, SCREEN_HEIGHT)

    pass_time = Decimal(time.perf_counter()).quantize(Decimal('1.0000'))
    nowtime = (pass_time - st_time) * 1000

    nt = font.render('time: ' + str(nowtime), False, Colors.WHITE)
    screen.blit(nt, (20, 60))

    # ノーツデータのキー値と経過時間が一致したノーツを出力
    if outNote:
        outNote = False
        offset = next(iter(SCORE))
        notes = SCORE.pop(offset)

    # ノーツのオフセットが経過時間(-1秒)になったらノーツを表示 
    # 表示中のノーツ
    if not outNote and (nowtime - Decimal('1.0000')) > Decimal(offset):
        for note in notes:
            disp_notes.append(note)

        outNote = True

    # pprint.pprint(disp_notes)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    for i, note in enumerate(disp_notes):
        dn = DispNotes(note['note'], note['x'], note['y'])
        dn.draw(screen)
        disp_notes[i]['y'] += 0.5

        if disp_notes[i]['y'] > SCREEN_HEIGHT:
            del disp_notes[i]

    pygame.display.update() 


            
