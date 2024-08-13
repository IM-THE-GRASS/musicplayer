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
    def set_volume(self, vol:int):
        print(type(vol))
        return rx.call_script(
            f"""pywebview.api.set_volume({vol[0]})"""
        )
    
    def resume1(self):
        print("AAA", self.active)
        if self.active:
            return self.resume()
        else:
            return self.play()
    
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