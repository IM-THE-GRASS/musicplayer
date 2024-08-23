import reflex as rx
from musicplayer.state import State

def icon_sidebar_button(icon:str, text:str, **props):
    return rx.button(
        rx.center(
            rx.icon(
                icon,
                width="30px",
                height="auto",
            ),  
            width="100%",
            height="100%"
        ),
        width="auto",
        height="30px",
        padding="4px",
        variant="ghost",
        color_scheme="gray",
        **props
    )
    


def sidebar():
    return rx.vstack(
        rx.vstack(
            icon_sidebar_button("home", "Home", on_click=State.set_current_page("home")),
            # icon_sidebar_button("search", "Search", on_click=State.set_current_page("search")),
            # icon_sidebar_button("library", "Your Library", on_click=State.set_current_page("library")),
            # icon_sidebar_button("heart", "Liked Songs", on_click=State.set_current_page("liked")),
            rx.dialog.root(
                rx.dialog.trigger(
                    icon_sidebar_button("plus", "Create Playlist"),
                ),
                rx.dialog.content(
                    rx.vstack(
                        rx.heading("Youtube playlist downloader"),
                        rx.input(
                            placeholder="Enter youtube playlist url here...",
                            value = State.playlist_url,
                            on_change= State.on_change_url,
                            width = "50vw"
                        ),
                        rx.input(
                            placeholder="Enter playlist name...",
                            width = "50vw",
                            value=State.playlist_name,
                            on_change=State.on_change_name
                        ),
                        rx.dialog.close(
                            rx.button(
                                "Confirm",
                                on_click=State.submit_playlist

                            )
                        )
                    )
                    
                )
            ),
            background="#121212",
            padding="22px",
            width="70px",
            border_radius="16px",
        ),
        rx.scroll_area(
            rx.vstack(
                rx.foreach(
                    State.playlistsinfo,
                    lambda info: rx.tooltip(rx.hstack(rx.image(src=info["image"], width = "44px", height= "44px",object_fit="cover", border_radius ="4px")), content=info["name"], side="right")
                    
                ),
                background="#121212",
                padding="13px",
                border_radius="16px",
                margin_top="16px",
                width="70px",
                height="40vh"
            ),
            width="70px",
            type="always",
            scrollbars="vertical"
        ),
        
        width="85px",
        padding="16px",
        bg="black",
    )