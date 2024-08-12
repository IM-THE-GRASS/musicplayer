import reflex as rx

class State(rx.State):
    current_page = "home"
    
    def set_current_page(self, new_page:str):
        self.current_page = new_page
        print(self.current_page)
        
    def pause(self):
        pass
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
    @rx.var
    def active(self):
        pass
    @rx.var
    def playing(self):
        pass
    @rx.var
    def paused(self):
        pass
    @rx.var
    def volume(self):
        pass
    