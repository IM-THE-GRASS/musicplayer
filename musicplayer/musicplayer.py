
import reflex as rx
from musicplayer.components.footer import *
from musicplayer.components.sidebar import *
from musicplayer.components.header import *
from musicplayer.components.maincontent import *
from musicplayer.components.nowplaying import *
from musicplayer.components.playlist import *



def log():
    return rx.call_script("pywebview.api.log(\"HELPME\")")



def index():
    return rx.box(
        rx.vstack(
            header(),
            rx.hstack(
                sidebar(),
                main_content(),
                now_playing(),
                height="100%",
                width="100%",
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