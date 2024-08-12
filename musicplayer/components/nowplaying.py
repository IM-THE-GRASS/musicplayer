import reflex as rx

def now_playing():
    return rx.vstack(
        rx.image(src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432", alt="Minecraft", width="100%", height="auto", object_fit="cover"),
        rx.text("Echo in the Wind (Monolism Remix)", font_weight="semibold"),
        rx.text("Minecraft, Monolism", color="gray.400", font_size="0.8em"),
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.text("Next in Queue", font_weight="bold"), 
                    rx.spacer()
                ),
                rx.hstack(
                    rx.center(
                        rx.icon("audio-lines"),
                        height="40px"
                    ),
                    rx.image(
                        src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432",
                        height="40px",
                        width="auto"
                    )
                )
            ),
            
            bg = "#1F1F1F",
            width="100%",
            padding="16px"
            
        ),
        bg = "#121212",
        width="400px",
        height="100%",
        padding="2em",
        margin="2em",
        position="relative",
        top="-50px"
        
    )