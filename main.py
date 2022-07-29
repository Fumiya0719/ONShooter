import pygame, sys, random, math, time, pprint
from pygame.locals import *
from screen import FixedScreen
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
# 譜面データから譜面本体を書き出す
SCORE = readMap.readMap(MAP['score'])
print(pprint.pprint(SCORE))

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