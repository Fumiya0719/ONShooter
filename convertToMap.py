# import pygame
# from pygame.locals import *
from notes import Notes
from decimal import *
import pprint

def convertToMap(file, speed, judge_point):
    MAP = {}

    FILE = open(file, 'r')
    title = FILE.readline()
    bpm = FILE.readline()
    title = title.rstrip('\n')
    bpm = Decimal(bpm.rstrip('\n'))

    MAP['title'] = title
    MAP['bpm'] = bpm
    MAP['score'] = []

    # 譜面データをノーツデータに変換
    timing = 0
    SCORE = FILE.readlines()
    for i, s in enumerate(SCORE):

        data = s.rstrip('\n')
        data = list(data)

        # リスト化したデータが空だった場合、次の小節へ
        if not data:
            beat = Decimal(60 * 1000 / bpm) * 4
            timing += beat
        else:
            # ノーツの間隔
            # 読み込んだデータの各行が4文字なら4分間隔, 8文字なら8分間隔... という形
            noteInterval = len(data)
            # 1ビートの間隔(ms)
            beat = Decimal(60 * 1000 / bpm) / Decimal(noteInterval / 4) 

            # ノーツの追加処理
            for j, d in enumerate(data):
                # 値が1の場合、ノーツを追加する
                if d == '1':
                    # ノーツ色,初期座標の判定 
                    # 行番を4で割った時の余りが↓
                    # 0 = 赤, 1 = 緑, 2 = 青
                    row = i % 4
                    if row == 0:
                        file = 'red.png'
                        x = 418
                    elif row == 1:
                        file = 'green.png'
                        x = 540
                    elif row == 2:
                        file = 'blue.png'
                        x = 662

                    # オフセット
                    offset = (timing + beat * j) + (1500 - (judge_point / speed))
                    offset = round(offset)
                    print(offset)

                    # ノーツの生成
                    note = Notes(file, x, 0, offset)
                    MAP['score'].append(note.makeNote())
            
    return MAP
