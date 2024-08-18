import reflex as rx
import musicplayer.state
class State(rx.State):
    current_page = "home"
    
    
    def set_current_page(self, new_page:str):
        self.current_page = new_page
        print(self.current_page)
        
    def pause(self):
        return rx.call_script(
            """pywebview.api.pause()"""
        )
    def play(self):
        return rx.call_script(
            """pywebview.api.play()"""
        )
    def resume(self):
        return rx.call_script(
            """pywebview.api.resume()"""
        )
    def stop(self):
        return rx.call_script(
            """pywebview.api.stop()"""
        )
    def skip_song(self):
        return rx.call_script(
            """pywebview.api.next_song()"""
        )
    def prev_song(self):
        return rx.call_script(
            """pywebview.api.previous_song()"""
        )
    def set_volume(self, vol:int):
        print(type(vol))
        return rx.call_script(
            f"""pywebview.api.set_volume({vol[0]})"""
        )
    def select_playlist(self, playlist:str):
        return rx.call_script(
            f"""pywebview.api.select_playlist("{playlist}")"""
        )
    def play_from_playlist(self, song_num):
        return rx.call_script(
            f"""pywebview.api.play_from_playlist("{song_num}")"""
        )
    def resume1(self):
        print("AAA", self.active)
        if self.active:
            return self.play_from_playlist(1)
        else:
            return self.play_from_playlist(1)
    
    playing:bool = True
    def get_playing(self, playing):
        self.playing = playing
    active:bool = True
    def get_active(self, active):
        self.active = active
    paused:bool = True
    def get_paused(self, paused):
        self.paused = paused
    volume:int = 1
    def get_volume(self, volume):
        self.volume = volume
    playlists:list[str]
    def get_playlists(self, playlists):
        self.playlists = playlists