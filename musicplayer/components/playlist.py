import reflex as rx
from musicplayer.state import State


def playlist_card(name:str, img:str = ""):
    return rx.vstack(
        rx.image(src=img, width="8em", height="8em", object_fit="cover", border_radius="4px",),
        rx.text(name, font_weight="semibold"),
        on_click=lambda: State.select_playlist(name),
        padding="8px",
        border_radius="4px",
        bg = "#121212",
        width="8em"
    )