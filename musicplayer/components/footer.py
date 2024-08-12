import reflex as rx


def footer():
    return rx.center(
        rx.hstack(
            
            rx.hstack(
                rx.image(src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432", width="auto", height="60px"),
                rx.vstack(
                    rx.text("Echo in the Wind (Monolism Remix)", font_weight="semibold", font_size="20px"),
                    rx.text("Monolism, Minecraft", font_weight="light", font_size="15px"),
                    align_items="start",
                    spacing="1"
                ),
                margin_left="10px",
                margin_top="0.5%"
            ),
            rx.spacer(),
            rx.hstack(
                rx.icon("shuffle"),
                rx.icon("skip-back"),
                rx.icon("play"),
                rx.icon("skip-forward"),
                rx.icon("repeat"),
                spacing="4",
                margin_top="20px",
            ),
            rx.spacer(),
            rx.hstack(
                rx.icon("volume-2"),
                rx.center(
                    rx.box(
                        rx.hstack(
                            rx.box(
                                width="75%",
                                height="4px",
                                bg="white",
                            ),
                            rx.box(
                                width="25%",
                                height="4px",
                                bg="#4D4D4D",
                            ),
                            width="100%",
                            spacing="0"
                        ),
                        
                        width="128px",
                        height="4px",
                    ),
                    
                    width="128px",
                    height="20px"
                ),
                margin_top="20px",
                margin_right="10px"
            ),
            height="70px",
            width="100%",
            
        ),
        
        height="96px",
        width="100%",
        bg = "#121212",
        padding="5px"
    )