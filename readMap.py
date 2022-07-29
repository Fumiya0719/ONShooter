import pygame, sys, math, time
from pygame.locals import *

# 譜面データ(Score)を音ゲーとして出力できる形式に変換する
def readMap(score):

    SCORE = {}

    # Scoreに登録されているノーツをオフセット毎に分類
    for note in score:
        offset = note['offset']

        note = {
            'note': note['note'],
            'x': note['x'],
            'y': note['y']
        }   

        if not offset in SCORE:
            SCORE[offset] = []

        SCORE[offset].append(note)

    sorted(SCORE.items())
    return SCORE
