import reflex as rx
import musicplayer.state
import os
from tinytag import TinyTag
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
    def download_playlist(self, url, playlist_name):
        return rx.call_script(
            f"""pywebview.api.download_playlist("{url}", "{playlist_name}")"""
        )
    def resume1(self):
        print("AAA", self.active)
        if self.active:
            return self.resume()
        else:
            return self.play_from_playlist(None)
    
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
    def get_playlist_img(self, playlist, reflex = False):
        path = os.path.join(os.getcwd(), "assets", "app", "music",playlist)
        
        exts:list = [".jpg", ".webp", ".png", ".jpeg"]
        for ext in exts:
            img_file = os.path.join(path, "playlist" + ext)
            if os.path.isfile(img_file):
                if reflex:
                    return os.path.join("app", "music", playlist, "playlist" + ext)
                return img_file
        return "https://cloud-46rupj524-hack-club-bot.vercel.app/0playlist-icon-768x432.png"
        
    playlists:list[str]
    playlistsinfo:list[dict[str, str]]
    def get_playlists(self, playlists):
        playlistsinfo:list[dict[str, str]] = []
        for playlist in playlists:
            playlistsinfo.append(
                {
                    "name":playlist,
                    "image":self.get_playlist_img(playlist,  True)
                }
            )
        self.playlistsinfo = playlistsinfo
            
        self.playlists = playlists
    current_playlist:str
    def get_current_playlist(self, playlist):
        self.current_playlist = playlist
    current_song_path:str
    current_song_img:str
    current_song_artist:str
    current_song_name:str
    
    def get_song_img(self, song):
        path = os.path.join("app", "music", self.current_playlist)
        exts:list = [".jpg", ".webp", ".png", ".jpeg"]
        
        music_file = os.path.join(path, song),
        music_file = music_file[0]
        tag = TinyTag.get(os.path.join(os.getcwd(), "assets", music_file))
        
        self.current_song_artist = tag.artist
        self.current_song_name = tag.title    
        for ext in exts:
            
            img_file = music_file.replace(".mp3", ext)
            if os.path.isfile(os.path.join(os.getcwd(), "assets", img_file)):
                return img_file
    
    def get_current_song(self, song):
        if not self.current_playlist or not song:
            return
        self.current_song = song
        self.current_song_img = self.get_song_img(song)
        print(self.playlists)
        
    
    
    playlist_url:str
    playlist_name:str
    def on_change_url(self, new):
        self.playlist_url = new
    def on_change_name(self, new):
        self.playlist_name = new
    def submit_playlist(self):
        return self.download_playlist(self.playlist_url, self.playlist_name)