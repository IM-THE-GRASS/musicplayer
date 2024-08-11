
import reflex as rx
from musicplayer.components.footer import *
from musicplayer.components.sidebar import *
from musicplayer.components.header import *




def log():
    return rx.call_script("pywebview.api.log(\"HELPME\")")



def index():
    return rx.box(
        rx.vstack(
            header(),
            rx.hstack(
                sidebar(),
                height="100%",
                overflow="hidden",
            ),
            footer(),
            height="100vh",
        ),
        bg="black",
        color="white",
    )











app = rx.App()
app.add_page(index)