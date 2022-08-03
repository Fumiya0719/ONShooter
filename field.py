import pygame
from pygame.locals import *
from colors import Colors
from decimal import *

class Field(pygame.sprite.Sprite, Colors):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def draw(self, screen, screen_width, screen_height):
        screen.fill(Colors.DGRAY)

        x = screen_width
        y = screen_height

        # yを5分割する(4:ノーツの出現位置(y=0), 1:判定ラインからノーツの消失点(y=高さ))
        judge_line = y/5 * 4