import pygame
from pygame.locals import *

class Notes(pygame.sprite.Sprite):
    def __init__(self, file):
        pygame.sprite.Sprite.__init__(self)

        # ノーツ画像の読み込み
        self.note = pygame.image.load(file)

        # ノーツ画像のリサイズ
        self.note = pygame.transform.scale(self.note, (120, 40))

    # ノーツの落下
    def fall(self, x, y):
        self.noteX = x
        self.noteY = y

    def draw(self, screen, beated):
        if not beated:
            screen.blit(self.note, (self.noteX, self.noteY))

        