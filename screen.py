import pygame
from pygame.locals import *
from colors import Colors

# 固定画面表示
class FixedScreen(pygame.sprite.Sprite, Colors):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def draw(self, screen, judge_line, x, y):
        screen.fill(Colors.BLACK)

        # 譜面ラインの設定
        xl = 233
        # for i in range(6):
        #     xl += 122 * i
        #     pygame.draw.line(screen, Colors.GRAY, (xl, 0), (xl, y), 2)
        pygame.draw.line(screen, Colors.GRAY, (233, 0), (233, y), 2)
        pygame.draw.line(screen, Colors.GRAY, (355, 0), (355, y), 2)
        pygame.draw.line(screen, Colors.GRAY, (477, 0), (477, y), 2)
        pygame.draw.line(screen, Colors.GRAY, (599, 0), (599, y), 2)   
        pygame.draw.line(screen, Colors.GRAY, (721, 0), (721, y), 2)   
        pygame.draw.line(screen, Colors.GRAY, (843, 0), (843, y), 2)   
        pygame.draw.line(screen, Colors.GRAY, (965, 0), (965, y), 2)   
        
        # 判定ラインの設定
        pygame.draw.line(screen, Colors.WHITE, (233,judge_line), (965,judge_line), 5)
