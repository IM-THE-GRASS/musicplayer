import reflex as rx
from musicplayer.components.playlist import *
def main_content():
    return rx.vstack(
        rx.heading("Good afternoon, Josh", size="2xl", margin_bottom="1em"),
        rx.flex(
            rx.foreach(
                rx.Var.range(1, 5),
                lambda _, index: playlist_card(f"Playlist {index}")   
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