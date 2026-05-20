import os
import sys
import random
import librosa
import struct

#難易度振り分け
#easy
def easy_map_make(mp3_map_name):
    try:

        #BPM判定関数
        beat_ms = bpm_analyzer(mp3_map_name)
        result_message(success=True)
    except Exception as e:
        print(f"エラーが発生しました: {e}\n")
        result_message(success=False)



#normal
def normal_map_make(mp3_map_name):
    try:
        #BPM判定関数
        beat_ms = bpm_analyzer(mp3_map_name)
        result_message(success=True) 
    except Exception as e:
        print(f"エラーが発生しました: {e}\n")
        result_message(success=False)



#difficult
def difficult_map_make(mp3_map_name):
    try:
        #BPM判定関数
        beat_ms = bpm_analyzer(mp3_map_name)
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
        
    print(f" 曲のBPM: {bpm}")

    beat = 60000 / bpm
    return int(beat)


#パターン関数



#結果出力
def result_message(success):
    if success:
        print("mapが正常に生成されました。")
    else:
        print("map生成に失敗しました。")
    sys.exit()

