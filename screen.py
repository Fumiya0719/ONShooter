import pygame
from pygame.locals import *
from colors import Colors

# 固定画面表示
class FixedScreen(pygame.sprite.Sprite, Colors):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def draw(self, screen, judge_line, y):
        screen.fill(Colors.BLACK)

        # 判定ラインの設定
        pygame.draw.line(screen, Colors.WHITE, (416,judge_line), (782,judge_line), 5)
        # 譜面ラインの設定
        pygame.draw.line(screen, Colors.GRAY, (416, 0), (416, y), 2)
        pygame.draw.line(screen, Colors.GRAY, (538, 0), (538, y), 2)
        pygame.draw.line(screen, Colors.GRAY, (660, 0), (660, y), 2)
        pygame.draw.line(screen, Colors.GRAY, (782, 0), (782, y), 2)   
        
