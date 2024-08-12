
import reflex as rx
from musicplayer.components.footer import *
from musicplayer.components.sidebar import *
from musicplayer.components.maincontent.homecontent import home_content
from musicplayer.components.maincontent.searchcontent import search_content
from musicplayer.components.nowplaying import *
from musicplayer.components.playlist import *
from musicplayer.state import State


def log():
    return rx.call_script("pywebview.api.log(\"HELPME\")")



def index():
    return rx.box(
        rx.vstack(
            rx.hstack(
                sidebar(),
                rx.cond(
                    State.current_page == "home",
                    home_content(),
                ),
                rx.cond(
                    State.current_page == "search",
                    search_content(),
                ),
                now_playing(),
                height="100%",
                width="100%",
                overflow="hidden",
            ),
            footer(),
            height="100vh",
            padding_top="20px"
        ),
        bg="black",
        color="white",
    )












app = rx.App(
    stylesheets=[
        
        "/styles.css",
    ],
)

app.add_page(index)