import reflex as rx
from musicplayer.state import State


def playlist_card(name):
    return rx.vstack(
        rx.image(src="https://cloud-46rupj524-hack-club-bot.vercel.app/0playlist-icon-768x432.png", width="8em", height="8em", object_fit="cover", border_radius="4px",),
        rx.text(name, font_weight="semibold"),
        on_click=lambda: State.select_playlist(name),
        padding="8px",
        border_radius="4px",
        bg = "#121212",
        width="8em"
    )