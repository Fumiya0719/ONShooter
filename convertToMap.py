import pygame
from pygame.locals import *
from decimal import *
import sys, pprint

def convertToMap(mapdata, speed, field_data):
    MAP = {}

    title = mapdata['title']
    bpm = Decimal(mapdata['bpm'])
    start = mapdata['offset']
    judge_point = field_data['judge_point']
    
    MAP['title'] = title
    MAP['bpm'] = bpm
    MAP['score'] = []

    # ノーツの大きさ

    # 譜面データをノーツデータに変換
    timing = 0
    for data in mapdata['map']:

        # BPMの更新
        if 'bpm' in data:
            bpm = data['bpm']
        # ノーツの間隔
        noteInterval = data['beat'] if 'beat' in data else len(data['notes_list'])
        # 1ビートの間隔(ms)
        beat = Decimal(60 * 1000 / bpm) / Decimal(noteInterval / 4) 

        # リスト化したデータが空だった場合、次の小節へ
        if not data['notes_list']:
            beat = Decimal(60 * 1000 / bpm) * 4
            timing += beat
        # ノーツ一覧を取得
        for j, notes in enumerate(data['notes_list']):
            # ノーツの追加処理
            # 赤緑青ノーツは複数同時があるので数を判定
            notes_red = 0
            notes_green = 0
            notes_blue = 0

            for note in notes:
                if note[0] == 'red': notes_red += 1 
                if note[0] == 'green': notes_green += 1 
                if note[0] == 'blue': notes_blue += 1 

                note_obj = {}
                # 画像ファイル名の作成
                file = note[0] + '.png'
                # ノーツ画像の読み込み
                note_img = pygame.image.load('images/' + file)
                pprint.pprint(field_data['note_sizex'])

                note_img = pygame.transform.scale(note_img, (
                    field_data['note_sizex'],
                    field_data['note_sizey']
                ))

                # オフセット
                offset = (timing + beat * j) + (Decimal(judge_point) / speed) + start
                offset = round(offset)

                # ノーツの生成
                if note[0] == 'red' and notes_red == 2:
                    note_obj['note_type'] = 'red2'
                elif note[0] == 'green' and notes_green == 2:
                    note_obj['note_type'] = 'green2'
                elif note[0] == 'blue' and notes_blue == 2:
                    note_obj['note_type'] = 'blue2'
                else:
                    note_obj['note_type'] = note[0]

                # ノーツ出現時のx座標
                if len(note) > 1:
                    note_obj['x'] = note[1]
                else:
                    sx7 = round(field_data['st_line_scale'] / 6)
                    # ndst = field_data['st_line_st'] + round(sx7 / 2)
                    ndst = field_data['st_line_st']
                    if note_obj['note_type'] == 'red': 
                        note_obj['x'] = ndst + (sx7 * 1) - (sx7 / 2)
                    if note_obj['note_type'] == 'green': 
                        note_obj['x'] = ndst + (sx7 * 2) - (sx7 / 2)
                    if note_obj['note_type'] == 'blue': 
                        note_obj['x'] = ndst + (sx7 * 3) - (sx7 / 2)
                    if note_obj['note_type'] == 'red2': 
                        note_obj['x'] = ndst + (sx7 * 4) - (sx7 / 2)
                    if note_obj['note_type'] == 'green2': 
                        note_obj['x'] = ndst + (sx7 * 5) - (sx7 / 2)
                    if note_obj['note_type'] == 'blue2': 
                        note_obj['x'] = ndst + (sx7 * 6) - (sx7 / 2)

                note_obj['note'] = note_img
                note_obj['offset'] = offset
                note_obj['y'] = 0
                note_obj['ln'] = note[2] if len(note) > 2 else False
                note_obj['ex'] = note[3] if len(note) > 3 else False                

                MAP['score'].append(note_obj)
           
    return MAP
