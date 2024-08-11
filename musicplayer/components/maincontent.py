import reflex as rx
from musicplayer.components.playlist import *
def main_content():
    return rx.vstack(
        rx.heading("Good afternoon", size="2xl", margin_bottom="1em"),
        rx.flex(
            rx.foreach(
                rx.Var.range(1, 15),
                lambda _, index: playlist_item(f"Playlist {index}", "Artist")   
            ),
            columns="2",
            flex_wrap="wrap",
            margin_bottom="2em",
        ),
        rx.heading("Made For you", size="xl", margin_bottom="1em"),
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