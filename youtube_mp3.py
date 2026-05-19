import os
import yt_dlp
import node_pattern as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#mp3生成
def download_youtube_as_mp3(youtube_url):

    ydl_opts = {
        'format': 'bestaudio/best',

        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],

        'postprocessor_args': ['-filter:a', 'volume=4dB'],
        'outtmpl': os.path.join(BASE_DIR, 'input_audio', '%(title)s.%(ext)s'),
        'ffmpeg_location': BASE_DIR,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        filename = ydl.prepare_filename(info)
        mp3_path = os.path.splitext(filename)[0] + '.mp3'
        return mp3_path


url = input("YouTubeのURLを入力してください: ")
mp3_map_name = download_youtube_as_mp3(url)


#フォルダ作成（ない場合）
folder_path = 'out_maps'
os.makedirs(folder_path, exist_ok=True)

#rhythia譜面作成
while True:

    print("\n--- ♡難易度を入力してください♡ ---")
    print("1. easy")
    print("2. normal")
    print("3. difficult")

    model = input()

    if model == "1":
        print("easy譜面を作成します")
        np.easy_map_make(mp3_map_name)
    elif model == "2":
        print("normal譜面を作成します")
        np.normal_map_make(mp3_map_name)
    elif model == "3":
        print("difficult譜面を作成します")
        np.difficult_map_make(mp3_map_name)
    else:
        print("1〜3の数字を入力してください。")