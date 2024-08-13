import reflex as rx

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
        pass
    def stop(self):
        pass
    def set_volume(self, vol:int):
        pass
    
    
    
    thing:bool = False
    def handle_thing(self, thing):
        print(thing)
        self.thing = thing
    def get_playing(self, _):
        print(_)
    