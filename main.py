import pygame, sys, pprint
from pygame.locals import *
from decimal import *
from screen import FixedScreen
from colors import Colors
from dispNotes import DispNotes
import convertToMap
import readMap

pygame.init() 

"""
スクリーン設定
"""
# 画面サイズ
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('C:/Windows/Fonts/Yu Gothic UI', 30)

pygame.display.set_caption('ONShooter')

"""
操作設定
"""
# 楽曲設定
MAPNAME = 'score1'
# ハイスピード設定
speed = 1
# キーコンフィグ
keyR = [pygame.K_s, pygame.K_j]
keyG = [pygame.K_d, pygame.K_k]
keyB = [pygame.K_f, pygame.K_l]

# 判定ライン・判定幅
judge_point = 600

# 譜面データの読み込み
MAPLINK = 'scores/' + MAPNAME + '/' + MAPNAME + '.txt'
MAP = convertToMap.convertToMap(MAPLINK, Decimal(speed), judge_point)
# 譜面データから譜面本体(ノーツデータ)を書き出す
SCORE = readMap.readMap(MAP['score'])
# print(SCORE)
# sys.exit()

SCREEN = FixedScreen()
running = True
outNote = True
point = 0
st_time = pygame.time.get_ticks()
disp_notes = []
offset = next(iter(SCORE))
notes = SCORE.pop(offset)
# ゲームの起動
while running:
    SCREEN.draw(screen, judge_point + 20, SCREEN_WIDTH, SCREEN_HEIGHT)

    pass_time = pygame.time.get_ticks()
    nowtime = pass_time - st_time

    pt = font.render('score: ' + str(point), False, Colors.WHITE)
    screen.blit(pt, (20, 40))
    nt = font.render('time: ' + str(round(nowtime / 1000, 2)), False, Colors.WHITE)
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
            dn = DispNotes(note['note'], note['x'], note['y'])
            dn.draw(screen)
            note['y'] = round((nowtime - note['st_time']) * Decimal(speed))

            if note['y'] > SCREEN_HEIGHT:
                del disp_notes[i]

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # キーが押された際の処理
        if event.type == pygame.KEYDOWN and notes:
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

    pygame.display.update() 


            
