import reflex as rx

class State(rx.State):
    current_page = "home"
    
    def set_current_page(self, new_page:str):
        self.current_page = new_page
        print(self.current_page)