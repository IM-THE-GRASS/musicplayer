import reflex as rx

def sidebar():
    return rx.vstack(
        rx.hstack(rx.icon("home"), rx.text("Home")),
        rx.hstack(rx.icon("search"), rx.text("Search")),
        rx.hstack(rx.icon("library"), rx.text("Your Library")),
        rx.hstack(rx.icon("heart"), rx.text("Liked Songs")),
        rx.hstack(rx.icon("plus"), rx.text("Create Playlist")),
        rx.vstack(
            rx.foreach(
                rx.Var.range(1, 5),
                lambda _, index: rx.hstack(rx.image(src="https://i.scdn.co/image/ab67616d00001e02bddf8d199ee35a13eddd1432", width = "5vw", height= "5vw"), rx.text("Playlist"))
                
            ),
            margin_top="16px",
        ),
        width="240px",
        padding="16px",
        bg="black",
    )