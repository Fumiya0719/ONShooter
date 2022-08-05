import pygame
from pygame.locals import *

class DispNotes(pygame.sprite.Sprite):
    # ノーツの定義
    def __init__(self, note, xs, xe, y, field_data):
        pygame.sprite.Sprite.__init__(self)

        self.xs = xs
        self.xe = xe
        self.y = y
        self.height = field_data['screen_height']

        self.sizex = field_data['note_sizex']
        self.sizey = field_data['note_sizey']

        self.note = note
        # ノーツのy座標に応じてスケールを変化
        self.note = pygame.transform.scale(self.note, (
            self.sizex + self.sizex * (4 / self.height * self.y) / 1.3,
            self.sizey + self.sizey * (4 / self.height * self.y) / 1.3
        ))

        self.x = self.xs + round(((self.xe - self.xs) / self.height) * self.y)

        self.rect = self.note.get_rect()
        self.rect.center = (self.x, self.y)

    # ノーツの表示
    def draw(self, screen):
        screen.blit(self.note, self.rect)

    # ノーツが出現した際の移動
    # def move(self, speed):
    #     self.rect.move_ip(0, 1 * speed)