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
            icon_sidebar_button("search", "Search", on_click=State.set_current_page("search")),
            icon_sidebar_button("library", "Your Library", on_click=State.set_current_page("library")),
            icon_sidebar_button("heart", "Liked Songs", on_click=State.set_current_page("liked")),
            rx.dialog.root(
                rx.dialog.trigger(
                    icon_sidebar_button("plus", "Create Playlist"),
                ),
                rx.dialog.content(
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.button("AA")
                        ),
                        rx.dialog.content(
                            rx.heading("EXAMPLE TEXT"),
                            rx.heading("HI")
                        )
                    ),
                    rx.heading("HELLO"),
                    rx.heading("HELLO"),
                    rx.heading("HELLO"),
                    rx.heading("HELLO"),
                    
                    rx.heading("HELLO"),
                    rx.dialog.close(
                        rx.button("Create Playlist"),
                    ),
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
                    rx.Var.range(1, 19),
                    lambda _, index: rx.hstack(rx.image(src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432", width = "100%", height= "auto", border_radius ="4px"))
                    
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