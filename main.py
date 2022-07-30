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
offset = next(iter(SCORE))
notes = SCORE.pop(offset)
# ゲームの起動
while running:
    SCREEN.draw(screen, judge_point + 20, SCREEN_HEIGHT)

    pass_time = Decimal(time.perf_counter()).quantize(Decimal('1.0000'))
    nowtime = (pass_time - st_time) * 1000

    nt = font.render('time: ' + str(nowtime), False, Colors.WHITE)
    screen.blit(nt, (20, 60))

    # ノーツのオフセットが経過時間になったら該当ノーツを表示キューに挿入
    if outNote and nowtime > Decimal(offset):
        for note in notes:
            disp_notes.append(note)

        if SCORE:
            offset = next(iter(SCORE))
            notes = SCORE.pop(offset)
        else:
            outNote = False

    # ノーツの表示と移動
    if disp_notes:
        pprint.pprint(disp_notes)
        for i, note in enumerate(disp_notes):
            dn = DispNotes(note['note'], note['x'], note['y'])
            dn.draw(screen)
            note['y'] += 0.6

            if note['y'] > SCREEN_HEIGHT:
                del disp_notes[i]

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update() 


            
