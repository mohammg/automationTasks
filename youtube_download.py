#pip install pytube
from pytube import YouTube,Playlist
import os
import sys
url_video=''
current_dir =os.path.dirname(os.path.realpath(__file__))
def download_video():
    yt=YouTube(url_video,on_progress_callback=on_progress)
    yt=yt.streams.get_highest_resolution()
    yt.download(current_dir)
    print("complete Download ",yt.title)

def download_playlist():
    ylist=Playlist(url_video)
    for p in ylist:
        print(p)
        
        single_video(p)
def single_video(url):
    yt=YouTube(url,on_progress_callback=on_progress)
    yt=yt.streams.get_highest_resolution()
    yt.download(current_dir)
    print("complete Download ",yt.title)
def on_progress(video_stream, total_size, bytes_remaining):
    total_size = video_stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print("\r" + "▌" * int(percent) + " " * (100 - int(percent)) + " {}%".format(int(percent)), end='')

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()

