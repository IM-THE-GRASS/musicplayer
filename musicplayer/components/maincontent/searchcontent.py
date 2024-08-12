import reflex as rx
from musicplayer.components.playlist import *


def search():
    return rx.hstack(
        rx.link(
            rx.icon(tag="search", color="white", size=30),
        ),
        rx.input(
            placeholder="Search",
            color="white",
            font_size="3.5vh",
            width="100%",
            background_color="rgba(255, 255, 255, 0)",
            border="none",
            border_width="0px",
            height="30",
        ),
        
        bg="rgba(0, 0, 0, 0.29)",
        border_radius="99999px",
        padding="0.5vh",
        width="48vw",
        # position="absolute",
        # left="28vw",
        # top="2vh",
    ),



def search_content():
    return rx.vstack(
        search(),
        rx.heading("Search", size="2xl", margin_bottom="1em"),
        rx.flex(
            rx.foreach(
                rx.Var.range(1, 5),
                lambda _, index: playlist_card(f"search result number {index}")   
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