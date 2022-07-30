import pygame
from pygame.locals import *

class DispNotes(pygame.sprite.Sprite):
    # ノーツの定義
    def __init__(self, note, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.note = note

        self.rect = note.get_rect()
        self.rect.center = ((x + x + 120) / 2, y)

    # ノーツの表示
    def draw(self, screen):
        screen.blit(self.note, self.rect)

    # ノーツが出現した際の移動
    # def move(self, speed):
    #     self.rect.move_ip(0, 1 * speed)