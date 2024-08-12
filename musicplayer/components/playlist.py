import reflex as rx

def playlist_item(title, artist):
    return rx.hstack(
        rx.image(src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432", alt=title, width="5em", height="5em"),
        rx.vstack(
            rx.text(title, font_weight="semibold"),
            rx.text(artist, font_size="sm"),
            align_items="start",
        ),
        bg = "#121212",
        width="17vw",
        padding="1em",
        margin="5px",
        border_radius="16px",
    )

def playlist_card(title):
    return rx.vstack(
        rx.image(src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432", alt=title, width="100%", height="8em", object_fit="cover"),
        rx.text(title, font_weight="semibold"),
        padding="8px",
        border_radius="8px",
        bg = "#121212",
    )