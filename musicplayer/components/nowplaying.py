import reflex as rx

def now_playing():
    return rx.vstack(
        rx.heading("Minecraft: Soothing Synths (Monolism Remix)", size="lg", margin_bottom="1em"),
        rx.image(src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432", alt="Minecraft", width="100%", height="16em", object_fit="cover"),
        rx.text("Echo in the Wind (Monolism Remix)", font_weight="semibold"),
        rx.text("Minecraft, Monolism", color="gray.400", font_size="0.8em"),
        width="20em",
        padding="1em",
    )