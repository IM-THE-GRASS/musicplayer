import webview
import time
import json
import os
import subprocess
import threading
from yt_dlp import YoutubeDL
from just_playback import Playback
playback = Playback("""C:\\Users\\user\\code\\musicplayer\\app\\Blocks - Minecraft Music Disc - C418 [q3IKwWgv1GE].webm""")
def read_settings(): 
    with open("settings.json", "r") as f:
        loaded_settings = json.load(f)
        return json.dumps(loaded_settings, indent=4)
playback.play()
print()
class Api():
    playlists:dict
    def play(self):
        playback.play()
        print("PLAY")
    def pause(self):
        playback.pause()
    def resume(self):
        playback.resume()
    def stop(self):
        playback.stop()
    def set_volume(self, vol):
        playback.set_volume(vol)
    def get_playing(_:str):
        return playback.playing
    def get_active(_:str):
        return playback.active
    def get_paused(_:str):
        print(playback.paused)
        return playback.paused
    def get_volume(_:str):
        return playback.volume
    
    for folder in os.listdir("music"):
        path = os.path.join("music", folder)
        if os.path.isdir(path):
            print(path, "THISISADIR")

    
    
    
    def download_playlist(self, url:str, playlist_name:str = "default"):
        if "youtube" in url:
            URLS = [url]
            options={
                "ffmpeg_location":os.path.join("music","ffmpeg.exe"),
                "format":"ba, hasaud, ext:mp3",
                "keepvideo":False,
                "finalext":"mp3"
            }
            with YoutubeDL(options) as ydl:
                ydl.download(URLS)
        elif "spotify" in url:
            def spot_dl():
                subprocess.run(f'{os.path.join("music","spotdl.exe")} {url} --ffmpeg {os.path.join("music","ffmpeg.exe")} --output {os.path.join("music", playlist_name)}')    
            thread = threading.Thread(target=spot_dl)
            thread.start()
    
        
def open_file_dialog(window):

    result = window.create_file_dialog(
        webview.FOLDER_DIALOG, allow_multiple=False
    )
    print(type(result))
    return result

window = webview.create_window(
    "localhost",
    url='localhost:3000',
    js_api=Api(),
)
def loop(w:webview.Window):
    while True: 
        time.sleep(0.1)
        print("AA")
a = Api()
a.download_playlist("https://music.youtube.com/playlist?list=PLxvJ3-kdDEEiOxO55t1LrDvkNtWzO-Ohx", "ipad")   
webview.start(
    # loop, 
    # window, 
    debug=True
 )