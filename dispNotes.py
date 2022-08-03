import pygame
from pygame.locals import *

class DispNotes(pygame.sprite.Sprite):
    # ノーツの定義
    def __init__(self, note, y, field_data):
        pygame.sprite.Sprite.__init__(self)

        self.note = note
        # ノーツのy座標に応じてスケールを変化
        self.note = pygame.transform.scale(self.note, (
            
        ))


        self.y = y

        self.rect = note.get_rect()
        self.rect.center = (x, y)

    # ノーツの表示
    def draw(self, screen):
        screen.blit(self.note, self.rect)

    # ノーツが出現した際の移動
    # def move(self, speed):
    #     self.rect.move_ip(0, 1 * speed)