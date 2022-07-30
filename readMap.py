from unicodedata import decimal
import pygame, sys, math, time
from pygame.locals import *

# 譜面データ(Score)を音ゲーとして出力できる形式に変換する
def readMap(score):

    arr = {}

    # scoreに登録されているノーツをオフセット毎に分類
    for note in score:
        offset = str(note['offset'])

        note = {
            'note': note['note'],
            'x': note['x'],
            'y': note['y']
        }   

        if not offset in arr:
            arr[offset] = []

        arr[offset].append(note)

    # 辞書にしたデータをキーの数値昇順に変換
    arg = sorted(arr, key=float)
    SCORE = {}
    for n in arg:
        SCORE[n] = arr[n]
    return SCORE
