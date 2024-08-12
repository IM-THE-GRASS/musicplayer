import reflex as rx

def icon_sidebar_button(icon:str, text:str):
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.icon(
                icon,
                width="100%",
                height="auto"
            )
        ),
        rx.hover_card.content(
            rx.text(text),
            side="right",
        ),
        
    )
    


def sidebar():
    return rx.vstack(
        rx.vstack(
            icon_sidebar_button("home", "Home"),
            icon_sidebar_button("search", "Search"),
            icon_sidebar_button("library", "Your Library"),
            icon_sidebar_button("heart", "Liked Songs"),
            icon_sidebar_button("plus", "Create Playlist"),
            background="#121212",
            padding="20px",
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