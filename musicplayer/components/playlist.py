import reflex as rx

def playlist_item(title, artist):
    return rx.hstack(
        rx.image(src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432", alt=title, width="5em", height="5em"),
        rx.vstack(
            rx.text(title, font_weight="semibold"),
            rx.text(artist, color="gray.400", font_size="sm"),
            align_items="start",
        ),
        bg="gray.800",
        padding="1em",
        border_radius="lg",
    )

def playlist_card(title):
    return rx.vstack(
        rx.image(src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432", alt=title, width="100%", height="8em", object_fit="cover"),
        rx.text(title, font_weight="semibold"),
        bg="gray.800",
        padding="1em",
        border_radius="lg",
    )