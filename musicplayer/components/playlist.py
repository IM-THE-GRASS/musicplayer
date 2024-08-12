import reflex as rx



def playlist_card(title):
    return rx.vstack(
        rx.image(src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432", alt=title, width="8em", height="8em", object_fit="cover", border_radius="4px",),
        rx.text(title, font_weight="semibold"),
        padding="8px",
        border_radius="4px",
        bg = "#121212",
        width="8em"
    )