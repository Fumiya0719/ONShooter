import pygame
from pygame.locals import *
import sys, random
import math
from screen import FixedScreen
from notes import Notes
import scores.score1 as map

pygame.init() 

"""
スクリーン設定
"""
# 画面サイズ
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# タイトル
pygame.display.set_caption('ONShooter')

"""
画面内設定
"""
# 色のデフォルト設定
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (200,200,200)

# ノーツデータ
note_red = pygame.image.load('red.png')
note_red = pygame.transform.scale(note_red, (120, 40))
note_green = pygame.image.load('green.png')
note_green = pygame.transform.scale(note_green, (120, 40))
note_blue = pygame.image.load('blue.png')
note_blue = pygame.transform.scale(note_blue, (120, 40))

def notes(note, x, y):
    screen.blit(note, (x, y))

# フォント設定
font = pygame.font.SysFont('C:/Windows/Fonts/Yu Gothic UI', 30)

# ノーツの移動
note_start = 0
note_end = SCREEN_HEIGHT

"""
操作設定
"""
btn_red1 = pygame.K_s
btn_green1 = pygame.K_d
btn_blue1 = pygame.K_f
btn_red2 = pygame.K_j
btn_green2 = pygame.K_k
btn_blue2 = pygame.K_l

# 楽曲関連の設定
TITLE = map.TITLE
BPM = map.BPM
# notes per second
NPM = (BPM / 60) / 1000
clock = pygame.time.Clock()

# ノーツの座標
xr = 418
yr = 0
xg = 540
yg = 0
xb = 662
yb = 0

# 判定ライン
judge_point = 560

score = 0
SCREEN = FixedScreen()
NR = Notes('red.png')
NG = Notes('green.png')
NB = Notes('blue.png')
br = False
bg = False
bb = False

# スコア表示
running = True
while running:
    SCREEN.draw(screen, 600, SCREEN_HEIGHT)

    message = font.render('score: ' + str(score), False, WHITE)
    screen.blit(message, (20,20)) 

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # ボタンが押された時の処理
        if event.type == pygame.KEYDOWN:          
            if not br and event.key == btn_red1 or event.key == btn_red2:
                if judge_point - 60 < yr and yr < judge_point + 60:
                    score += 1
                    br = True
                    NR.remove()
                if judge_point - 20 < yr and yr < judge_point + 20:
                    score += 1

            elif not bg and event.key == btn_green1 or event.key == btn_green2:
                if judge_point - 60 < yg and yg < judge_point + 60:
                    score += 1
                    bg = True
                    NG.remove()
                if judge_point - 20 < yg and yg < judge_point + 20:
                    score += 1

            elif not bb and event.key == btn_blue1 or event.key == btn_blue2:
                if judge_point - 60 < yb and yb < judge_point + 60:
                    score += 1
                    bb = True
                    NB.remove()
                if judge_point - 20 < yb and yb < judge_point + 20:
                    score += 1
      
    yr += 0.5
    yg += 0.5
    yb += 0.5
    if yr == SCREEN_HEIGHT:
        yr = 0
    if yg == SCREEN_HEIGHT:
        yg = 0
    if yb == SCREEN_HEIGHT:
        yb = 0
    NR.fall(418, yr)
    NG.fall(540, yr)
    NB.fall(662, yr)
    NR.draw(screen, br)
    NG.draw(screen, bg)
    NB.draw(screen, bb)
    pygame.display.update()