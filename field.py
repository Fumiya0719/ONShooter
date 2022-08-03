import pygame,pprint
from pygame.locals import *
from colors import Colors
from decimal import *

class Field(pygame.sprite.Sprite, Colors):
    def __init__(self, screen, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.x = screen_width
        self.y = screen_height

    # 描写に必要なデータの準備
    def setData(self):
        self.screen.fill(Colors.DGRAY)

        # yを5分割する(4:ノーツの出現位置(y=0), 1:判定ラインからノーツの消失点(y=高さ))
        self.judge_line = self.y/5 * 4

        # フィールドの大きさ(デフォルト値)
        # ノーツ出現位置(y=0)
        self.field_scale_st = round(Decimal(self.judge_line / 3.22))
        # ノーツ消失点
        self.field_scale_ed = self.field_scale_st * 5

        # 画面の中央
        self.mid = self.x / 2

        # フィールド生成の始点x
        # ノーツ出現位置(y=0)
        self.field_st_st = self.mid - round(self.field_scale_st / 2)
        # ノーツ消失点
        self.field_st_ed = self.mid - round(self.field_scale_ed / 2)

        # フィールド生成の終点x
        # ノーツ出現位置(y=0)
        self.field_ed_st = self.field_st_st + self.field_scale_st
        # ノーツ消失点
        self.field_ed_ed = self.field_st_ed + self.field_scale_ed

        # フィールド描写用の線分リストの作成
        self.lines = []
        for i in range(self.y):
            if i == 0:
                self.lines.append([(self.field_st_st, i), (self.field_ed_st, i)])
            else:
                xs = self.field_st_st - round((self.field_scale_st * 2  / self.y) * i)
                xe = self.field_ed_st + round((self.field_scale_st * 2 / self.y) * i)
                self.lines.append([(xs, i), (xe, i)])

                if i == self.judge_line:
                    self.field_st_jg = xs
                    self.field_ed_jg = xe
                    self.field_scale_jg = xe - xs
                
        return {
            'screen_width': self.x,
            'screen_height': self.y,
            'judge_point': self.judge_line,
            'judge_line_scale': self.field_scale_jg,
            'st_line_st': self.field_st_st,
            'st_line_ed': self.field_ed_st,
            'st_line_scale': self.field_ed_st - self.field_st_st
        }

    # フィールドの描画
    def draw(self, screen):
        for line in self.lines:
            pygame.draw.aaline(screen, Colors.BLACK, line[0], line[1])            
        pygame.draw.line(screen, Colors.ORANGE, (self.field_st_jg, self.judge_line), (self.field_ed_jg, self.judge_line), 5)

        