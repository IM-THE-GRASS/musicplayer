import reflex as rx


def footer():
    return rx.hstack(
        rx.hstack(
            rx.image(src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432", alt="Currently Playing", width="48px", height="48px"),
            rx.vstack(
                rx.text("Echo in the Wind (Monolism Remix)", font_weight="semibold", font_size="10px"),
                align_items="start",
            ),
        ),
        rx.spacer(),
        rx.hstack(
            rx.icon("shuffle"),
            rx.icon("skip-back"),
            rx.icon("play"),
            rx.icon("skip-forward"),
            rx.icon("repeat"),
            spacing="4",
        ),
        rx.spacer(),
        rx.hstack(
            rx.text("2:03"),
            rx.center(
                rx.box(
                    rx.box(
                        width="50%",
                        height="4px",
                        bg="white",
                    ),
                    width="128px",
                    height="4px",
                ),
                
                width="128px",
                height="20px"
            ),
            
            rx.text("4:21"),
        ),
        height="64px",
        width="100%"
    )