import pygame
from pygame.locals import *
from colors import Colors
from decimal import *

class Field(pygame.sprite.Sprite, Colors):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    # 描写に必要なデータの準備
    def setData(self, screen, screen_width, screen_height):
        screen.fill(Colors.DGRAY)

        self.x = screen_width
        self.y = screen_height

        # yを5分割する(4:ノーツの出現位置(y=0), 1:判定ラインからノーツの消失点(y=高さ))
        self.judge_line = self.y/5 * 4

        # フィールドの大きさ(デフォルト値)
        # ノーツ出現位置(y=0)
        self.field_scale_st = round(Decimal(self.judge_line / 3.22))
        # 判定ライン
        self.field_scale_jg = self.field_scale_st * 4
        # ノーツ消失点
        self.field_scale_ed = self.field_scale_st * 5

        # 画面の中央
        self.mid = self.x / 2

        # フィールド生成の始点x
        # ノーツ出現位置(y=0)
        self.field_st_st = self.mid - round(self.field_scale_st / 2)
        # 判定ライン
        self.field_st_jg = self.mid - round(self.field_scale_jg / 2)
        # ノーツ消失点
        self.field_st_ed = self.mid - round(self.field_scale_ed / 2)

        # フィールド生成の終点x
        # ノーツ出現位置(y=0)
        self.field_ed_st = self.field_st_st + self.field_scale_st
        # 判定ライン
        self.field_ed_jg = self.field_st_jg + self.field_scale_jg
        # ノーツ消失点
        self.field_ed_ed = self.field_st_ed + self.field_scale_ed

        # フィールド描写用の線分リストの作成
        self.lines = []
        for i in range(self.y):
            if i == 0:
                self.lines.append([(self.field_st_st, i), (self.field_ed_st, i)])
            else:
                xs = self.field_st_st - round((self.field_scale_ed / self.y) * i)
                xe = self.field_st_st + round((self.field_scale_ed / self.y) * i)
                self.lines.append([(xs, i), (xe, i)])

        return self.judge_line

    # フィールドの描画
    def draw(self, screen):
        pygame.draw.aalines(screen, Colors.BLACK, True, self.lines)
        pygame.draw.line(screen, Colors.ORANGE, (self.field_st_jg, self.judge_line), (self.field_ed_jg, self.judge_line), 5)

        