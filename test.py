import pygame
from pygame.locals import *
import sys, random

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

# ノーツデータ
note_red = pygame.image.load('red.png')
note_green = pygame.image.load('green.png')
note_blue = pygame.image.load('blue.png')

def notes(x, y):
    screen.blit(note_red, (x, y))

# 背景色
bgc = (BLACK)
screen.fill(bgc)

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

# ノーツの座標
x = 480
y = 0

# 判定ライン
judge_line = 600
judge_point = judge_line - 80

score = 0
running = True
while running:
    # 背景の設定
    screen.fill(BLACK)
    # 判定ラインの設定
    pygame.draw.line(screen, WHITE, (0,judge_line), (1200,judge_line), 5)

    message = font.render('score: ' + str(score), False, WHITE)
    screen.blit(message, (20,20))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # ボタンが押された時の処理
        if event.type == pygame.KEYDOWN:
            if event.key == btn_red1 or event.key == btn_red2:
                if judge_point - 20 < y and y < judge_point + 20:
                    score += 2
                elif judge_point - 60 < y and y < judge_point + 60:
                    score += 1
                
    y += 0.5
    if y == SCREEN_HEIGHT:
        y = 0
    notes(x, y)
    pygame.display.update()