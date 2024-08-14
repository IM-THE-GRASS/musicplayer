import webview
import time
import json
import os
from just_playback import Playback
playback = Playback()
playback.load_file('play.mp3')
def read_settings(): 
    with open("settings.json", "r") as f:
        loaded_settings = json.load(f)
        return json.dumps(loaded_settings, indent=4)


class Api():
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
# def loop(w:webview.Window):
#     while True: 
#         time.sleep(0.1)
        
webview.start(
    # loop, 
    # window, 
    debug=True
 )