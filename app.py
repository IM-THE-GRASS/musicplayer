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
    def pause():
        playback.pause()
    def resume():
        playback.resume()
    def stop():
        playback.stop()
    def set_volume(vol):
        playback.set_volume(vol)
    
    def get_playing():
        return playback.playing
    def get_active():
        return playback.active
    def get_paused():
        return playback.paused
    def get_volume():
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
def loop(w:webview.Window):
    def send(to_send):
        w.evaluate_js(f"receive(\"{to_send}\")")
    while True: 
        time.sleep(0.1)
        # try:
        #     send("hello")
        # except:
        #     print("didnt work")
        
webview.start(loop, window, debug=True)