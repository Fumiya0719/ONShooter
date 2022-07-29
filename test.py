import pygame
from pygame.locals import *
import sys, random
import math
from screen import FixedScreen
from notes import Notes
import time

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

# 色のデフォルト設定
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (200,200,200)

"""
操作設定
"""
keyR = [pygame.K_s, pygame.K_j]
keyG = [pygame.K_d, pygame.K_k]
keyB = [pygame.K_f, pygame.K_l]

# 楽曲関連の設定
SF = open('scores/score1.txt', 'r')
TITLE = SF.readline()
bpm = int(SF.readline())
mapData = SF.readlines()
print(mapData)
sys.exit()

# 判定ライン
judge_point = 560
SCREEN = FixedScreen()

running = True
# ゲームの起動
while running:
    SCREEN.draw(screen, 600, SCREEN_HEIGHT)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
    pygame.display.update()