import os
import sys

#難易度振り分け
#easy
def easy_map_make(url):
    try:
        result_message(success=True)
    except Exception as e:
        print(f"エラーが発生しました: {e}\n")
        result_message(success=False)

#usually
def usually_map_make(url):
    try:
        result_message(success=True) 
    except Exception as e:
        print(f"エラーが発生しました: {e}\n")
        result_message(success=False)

#diffcult
def diffcult_map_make(url):
    try:
        result_message(success=True) 
    except Exception as e:
        print(f"エラーが発生しました: {e}\n")
        result_message(success=False)


#パターン関数

#結果出力
def result_message(success):
    if success:
        print("mapが正常に生成されました。")
    else:
        print("map生成に失敗しました。")
    sys.exit()

