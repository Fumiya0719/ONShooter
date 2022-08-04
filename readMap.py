# 譜面データ(Score)を音ゲーとして出力できる形式に変換する
def readMap(score, field_data):

    arr = {}

    # scoreに登録されているノーツをオフセット毎に分類
    for note in score:
        offset = note['offset']

        note = {
            'note': note['note'],
            'note_type': note['note_type'],          
            'xs': note['xs'],
            'xe': note['xe'],
            'y': note['y'],
            'ln': note['ln'],
            'ex': note['ex']
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
