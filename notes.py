import pygame
from pygame.locals import *
from decimal import *

class Notes(pygame.sprite.Sprite):
    # ノーツの定義
    def __init__(self, file, x, y, offset):
        pygame.sprite.Sprite.__init__(self)

        # ノーツの色の判定
        if file == 'red.png':
            self.noteType = 'red'
        elif file == 'green.png':
            self.noteType = 'green'
        elif file == 'blue.png':
            self.noteType = 'blue'

        # ノーツ画像の読み込み
        self.note = pygame.image.load(file)

        # ノーツ画像のリサイズ
        self.note = pygame.transform.scale(self.note, (120, 20))

        # 初期位置の座標設定
        self.x = x
        self.y = y

        # not(表示するタイミング)
        # 判定ラインに重なるタイミング
        self.offset = offset

    def makeNote(self):
        return {
            'note': self.note,
            'note_type': self.noteType,
            'x': self.x,
            'y': self.y,
            'offset': self.offset
        }





        