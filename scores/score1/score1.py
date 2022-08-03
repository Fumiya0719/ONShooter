MAPDATA = {
    'title': 'TestSong1',
    'bpm': 135,
    'offset': 580,
    # 譜面データ
    'map': [
        # bpm: 変更があれば記入
        # beat: 4分音符なら4, 8分音符なら8のように記述
        # data: 譜面の内容
        {
            'bpm': 135,
            'beat': 4,
            'notes_list': [
            # notes: 譜面の種類(
            # 単押し: red, green, blue
            # サイド: sidel, sider
            # ロングノーツ: 接頭辞ln_
            # ロングノーツ(終点): 接頭辞en_
            # フリック: flickl, flickr
            # )
            # cood: 座標(x, max=940) 無記入なら初期値
            # ln: ロングノーツの始点かどうか(bool) 無記入ならFalse
            # ex: ex-tapかどうか(bool) 無記入ならFalse
                [
                    ['red'],
                    ['blue'],
                    ['red'],
                ],
                [],
                [
                    ['red'],
                    ['blue'],
                    ['red'],
                ],
                [],
            ]
        },
        {
            'beat': 4,
            'notes_list': [
                [
                    ['red'],
                    ['red'],
                ],
                [
                    ['blue'],
                    ['blue'],
                ],
                [
                    ['green'],
                    ['green'],
                ],
                [
                    ['red'],
                    ['blue'],
                    ['green'],
                    ['red'],
                    ['blue'],
                    ['green'],
                ],
            ]
        }
    ]
}