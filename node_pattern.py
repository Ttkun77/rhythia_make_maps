import os
import sys
import random
import librosa
import struct


# 出力先フォルダの定義
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_MAPS_DIR = os.path.join(BASE_DIR, 'out_maps')
os.makedirs(OUT_MAPS_DIR, exist_ok=True)

# 文字列をSSPMのバイナリ形式（[長さ(1バイト)] + [文字列]）に変換する補助関数
def pack_string(string_data):
    encoded = string_data.encode('utf-8')
    return struct.pack('B', len(encoded)) + encoded

#難易度振り分け
#easy
def easy_map_make(mp3_map_name):
    try:

        #BPM判定関数
        beat_ms = bpm_analyzer(mp3_map_name)

        # 2. mp3ファイル自体のバイナリデータを読み込む
        with open(mp3_map_name, 'rb') as f:
            audio_bytes = f.read()

        # 曲名などの情報を取得
        mp3_filename = os.path.basename(mp3_map_name)
        song_title = os.path.splitext(mp3_filename)[0]

        # ★★★ ここを改造するだけ！ノーツデータの生成 (1拍ごとにノーツを置く) ★★★
        notes = create_pattern_notes(beat_ms, duration_sec=90)
        
        # 3. SSPMバイナリ全体の組み立て (パズルのようにガッチャンコする)
        buffer = bytearray()
        
        # ① 固定の合言葉
        buffer.extend(b'SS+m')
        
        # ② メタデータ（カスタムデータのヘッダー構造を本物に合わせる）
        buffer.extend(struct.pack('<I', 1))     # ダミーID
        buffer.extend(pack_string(song_title))  # 曲名
        buffer.extend(pack_string("AI_Mapper")) # 制作者名
        buffer.extend(pack_string("Easy"))      # 難易度名
        
        # ③ 音声データ（サイズ + 本体）
        buffer.extend(struct.pack('<I', len(audio_bytes)))
        buffer.extend(audio_bytes)
        
        # ④ ノーツの合言葉 "ssp_note" と 総ノーツ数
        buffer.extend(b'ssp_note')
        buffer.extend(struct.pack('<I', len(notes)))
        
        # ⑤ 改造されたノーツデータ（12バイトセット）をひたすら追加
        for note in notes:
            # <Iff = 4バイト整数(Time), 4バイト小数(X), 4バイト小数(Y) をリトルエンディアンで変換
            note_binary = struct.pack('<Iff', note['time'], note['x'], note['y'])
            buffer.extend(note_binary)

        # 4. 完成したバイナリをファイルとして書き出し
        output_filename = f"{song_title}_Easy.sspm"
        output_path = os.path.join(OUT_MAPS_DIR, output_filename)
        
        with open(output_path, 'wb') as f:
            f.write(buffer)

        result_message(success=True)
    except Exception as e:
        print(f"エラーが発生しました: {e}\n")
        result_message(success=False)



#normal
def normal_map_make(mp3_map_name):
    try:
        #BPM判定関数
        bpm_num = bpm_analyzer(mp3_map_name)
        result_message(success=True) 
    except Exception as e:
        print(f"エラーが発生しました: {e}\n")
        result_message(success=False)



#difficult
def difficult_map_make(mp3_map_name):
    try:
        #BPM判定関数
        bpm_num = bpm_analyzer(mp3_map_name)
        result_message(success=True) 
    except Exception as e:
        print(f"エラーが発生しました: {e}\n")
        result_message(success=False)


#BPM判定
def bpm_analyzer(mp3_map_name):

    print(f"\n[解析中] 音声ファイルを読み込んでいます...\n{mp3_map_name}")
    y, sr = librosa.load(mp3_map_name, sr=None)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    if hasattr(tempo, '__len__'):
        bpm = int(tempo[0])
    else:
        bpm = int(tempo)
        
    print(f"==========================================")
    print(f" 曲のBPM: {bpm}")
    print(f"==========================================")

    beat = 60000 / bpm
    return int(beat)


#パターン関数
def create_pattern_notes(beat_ms, duration_sec=90):
    notes_list = []
    total_ms = duration_sec * 1000  # 90秒間分
    
    current_ms = 0
    while current_ms < total_ms:
        # X座標は -2.0 〜 2.0、Y座標は -1.0 〜 1.0 の間でランダムに浮動小数を生成
        note_x = float(random.randint(-2, 2))
        note_y = float(random.randint(-1, 1))
        
        notes_list.append({
            "time": current_ms,  # ミリ秒（整数）
            "x": note_x,         # X（小数）
            "y": note_y          # Y（小数）
        })
        
        current_ms += beat_ms  # 1拍分進める
        
    return notes_list


#結果出力
def result_message(success):
    if success:
        print("mapが正常に生成されました。")
    else:
        print("map生成に失敗しました。")
    sys.exit()

