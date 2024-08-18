import reflex as rx
from musicplayer.components.playlist import *
from musicplayer.state import State
def home_content():
    return rx.vstack(
        rx.heading("Good afternoon, Josh", size="2xl", margin_bottom="1em"),
        rx.flex(
            rx.foreach(
                State.playlists,
                lambda name: playlist_card(name)   
            ),
            flex_wrap="wrap",
            columns="3",
            spacing="4",
        ),
        padding="1em",
        overflow_y="auto",
        height="100%",
        width="100%"
    )