import webview
import time
import json
import os
import subprocess
import threading
from yt_dlp import YoutubeDL
from just_playback import Playback
import random

playback = Playback()
def read_settings(): 
    with open("settings.json", "r") as f:
        loaded_settings = json.load(f)
        return json.dumps(loaded_settings, indent=4)


class Api():
    def load_playlists(output:dict):
        for folder in os.listdir("music"):
            path = os.path.join("music", folder)
            if os.path.isdir(path):
                output[folder] = [f for f in os.listdir(path) if f.endswith('.mp3')]
    playlists:dict = {}
    current_playlist = None
    current_song_songnum:int
    load_playlists(playlists)
    print(playlists)
    def play(self):
        if self.current_playlist and self.current_song_songnum >= 0:
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
    
    
    
    def get_playlists(self):
        return list(self.playlists.keys())
    def select_playlist(self, playlist_name):
        if playlist_name in self.playlists:
            self.current_playlist = playlist_name
            self.current_song_songnum = -1
    def play_from_playlist(self, songnum=None):
        if not self.current_playlist:
            return
        if songnum == None:
            songnum = self.current_song_songnum
            if songnum == -1:
                songnum = 0
        playlist = self.playlists[self.current_playlist]
        if songnum in range(len(playlist)):
            self.current_song_songnum = songnum
            song_path = os.path.join("music", self.current_playlist, playlist[songnum])
            playback.load_file(song_path)
            playback.play()

    def next_song(self):
        if self.current_playlist:
            next_songnum = (self.current_song_songnum + 1) % len(self.playlists[self.current_playlist]) # this line is ai :grin:
            self.play_from_playlist(next_songnum)
    def previous_song(self):
        if self.current_playlist:
            prev_songnum = (self.current_song_songnum - 1) % len(self.playlists[self.current_playlist])
            return self.play_from_playlist(prev_songnum)
        
    def shuffle_playlist(self):
        if self.current_playlist:
            random.shuffle(self.playlists[self.current_playlist])
            self.current_song_songnum = -1
    def get_current_song(self):
        if self.current_playlist and 0 <= self.current_song_songnum < len(self.playlists[self.current_playlist]):
            return self.playlists[self.current_playlist][self.current_song_songnum]
        return None

    def download_playlist(self, url:str, playlist_name:str = "default"):
        ffmpeg = os.path.join("music","ffmpeg.exe")
        if "youtube" in url:
            def youtube_download():
                options={
                    'format':'bestaudio/best',
                    'extractaudio':True,
                    'audioformat':'mp3',
                    "ffmpeg_location":ffmpeg,
                    "keepvideo":False,
                    "paths":{"home":os.path.join("music", playlist_name)},
                    "writeinfojson":True,
                    "writethumbnail":True,
                    "clean_infojson":True,
                    'postprocessors': [
                        {
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        },
                        {
                            'key': 'FFmpegMetadata'
                        }
                    ] # YIPPE I TOOK THIS FROM STACKOVERFLOW AND TI SOLVES ALL MYT PROBLEMS !!!!
                }
                with YoutubeDL(options) as ydl:
                    ydl.download([url])
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

a = Api()
a.select_playlist("MC LOFI")
a.play_from_playlist()
print(a.get_current_song())
a.shuffle_playlist()
while True:
    time.sleep(5)
    a.previous_song()
    
    print(a.get_current_song())
webview.start(
    debug=True
 )