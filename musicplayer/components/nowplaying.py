import reflex as rx
from musicplayer.state import State

def now_playing():
    return rx.vstack(
        rx.image(
            src=State.current_song_img,
            width="100%",
            height="13vw",
            object_fit="cover",
            border_radius="8px",
        ),
        rx.text(State.current_song_name, font_weight="semibold"),
        rx.text(State.current_song_artist, color="gray.400", font_size="0.8em"),
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
                    ),
                    rx.vstack(
                        rx.text("Echo in the wind...", font_size="0.8em"),
                        rx.text("Minecraft, Monolism", font_size="0.7em"),
                        spacing="0",
                        width="100%"
                        
                    )
                )
            ),
            
            bg = "#1F1F1F",
            width="100%",
            padding="16px"
            
        ),
        bg = "#121212",
        width="500px",
        height="100%",
        padding="2em",
        margin="2em",
        border_radius="8px",
    )