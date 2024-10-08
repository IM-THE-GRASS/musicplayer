import reflex as rx
from musicplayer.state import State

def footer():
    return rx.center(
        rx.hstack(
            
            rx.hstack(
                rx.image(
                    src="https://cloud-46rupj524-hack-club-bot.vercel.app/0playlist-icon-768x432.png",
                    width="60px",
                    height="60px",
                    object_fit="cover"
                ),
                rx.vstack(
                    rx.text(State.current_playlist, font_weight="semibold", font_size="20px"),
                    rx.text("", font_weight="light", font_size="15px"),
                    align_items="start",
                    spacing="1"
                ),
                margin_left="10px",
                margin_top="0.5%"
            ),
            rx.spacer(),
            rx.hstack(
                rx.button(
                    rx.icon("skip-back", size=40),
                    variant="ghost",
                    padding="0",
                    as_child=True,
                    on_click=State.prev_song
                ),
                
                rx.cond(
                    State.playing,
                    
                    rx.button(
                        rx.icon("pause", size=40),
                        on_click=State.pause,
                        variant="ghost",
                        padding="0",
                        as_child=True
                    ),
                    rx.button(
                        rx.icon("play", size=40),
                        on_click=State.resume1,
                        variant="ghost",
                        padding="0",
                        as_child=True
                    ),
                ),
                rx.moment(
                    on_change=[
                        rx.call_script("""pywebview.api.get_playing()""",callback=State.get_playing),
                        rx.call_script("""pywebview.api.get_paused()""",callback=State.get_paused),
                        rx.call_script("""pywebview.api.get_volume()""",callback=State.get_volume),
                        rx.call_script("""pywebview.api.get_active()""",callback=State.get_active),
                        rx.call_script("""pywebview.api.get_playlists()""",callback=State.get_playlists),
                        rx.call_script("""pywebview.api.get_current_song()""",callback=State.get_current_song),
                        rx.call_script("""pywebview.api.get_current_playlist()""",callback=State.get_current_playlist),
                    ],
                    interval=100,
                    position="absolute",
                    left="10000px",
                    overflow= "hidden"
                ),
                rx.button(
                    rx.icon("skip-forward", size=40),
                    variant="ghost",
                    padding="0",
                    as_child=True,
                    on_click=State.skip_song
                ),
                
                spacing="6",
                margin_top="10px",
                overflow= "hidden"
            ),
            rx.spacer(),
            rx.hstack(
                rx.icon("volume-2"),
                rx.center(
                    rx.box(
                        rx.slider(
                            color_scheme="gray",
                            radius="full",
                            high_contrast=True,
                            min=0,
                            max=1,
                            step=0.05,
                            on_change=State.set_volume
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