import pygame
from pygame.locals import *
from colors import Colors

# 固定画面表示
class FixedScreen(pygame.sprite.Sprite, Colors):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def draw(self, screen, judge_line, x, y, note_size):
        screen.fill(Colors.BLACK)

        frame_thick = 2
        frame_x = (x / 2) - ((note_size + frame_thick) * 3)
        frame_xo = frame_x
        frame_xe = frame_x + ((note_size + frame_thick) * 6)

        for i in range(7):
            pygame.draw.line(screen, Colors.GRAY, (frame_x, 0), (frame_x, y), frame_thick)
            frame_x += note_size + frame_thick
   
        # 判定ラインの設定
        pygame.draw.line(screen, Colors.WHITE, (frame_xo ,judge_line), (frame_xe, judge_line), 5)
