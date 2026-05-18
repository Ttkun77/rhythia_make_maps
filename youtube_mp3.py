import os
import yt_dlp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
        ydl.download([youtube_url])

url = input("YouTubeのURLを入力してください: ")
download_youtube_as_mp3(url)