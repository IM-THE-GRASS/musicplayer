import webview
import time
import json
import os
import subprocess
import threading
from yt_dlp import YoutubeDL
from just_playback import Playback
playback = Playback()
def read_settings(): 
    with open("settings.json", "r") as f:
        loaded_settings = json.load(f)
        return json.dumps(loaded_settings, indent=4)


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
        ffmpeg = os.path.join("music","ffmpeg.exe")
        if "youtube" in url:
            def youtube_download():
                options={
                    "ffmpeg_location":ffmpeg,
                    "format":"ba, hasaud",
                    "keepvideo":False,
                    "paths":{"home":os.path.join("music", playlist_name)}
                }
                with YoutubeDL(options) as ydl:
                    ydl.download([url])
                #convert to mp3 with ffmpeg
                for file in os.listdir(os.path.join("music", playlist_name)):
                    output = file.split(".")[0] + ".mp3"
                    output = os.path.join("music", playlist_name, output)
                    file = os.path.join("music",playlist_name, file)
                    if os.path.isfile(file):
                        subprocess.run(f'{ffmpeg} -i "{file}" "{output}"')
                #removes the non mp3 files
                for file in os.listdir(os.path.join("music", playlist_name)):
                    if not file.endswith(".mp3"):
                        file = os.path.join("music",playlist_name, file)
                        os.remove(file)
            thread = threading.Thread(target=youtube_download)
            thread.start()
        elif "spotify" in url:
            def spot_dl():
                subprocess.run(f'{os.path.join("music","spotdl.exe")} {url} --ffmpeg {ffmpeg} --output {os.path.join("music", playlist_name)}')    
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
a.download_playlist("https://www.youtube.com/playlist?list=PLZw5GZkde4STJs3666UWjbz-AXxOTx3Kt", "MC LOFI")   
webview.start(
    # loop, 
    # window, 
    debug=True
 )