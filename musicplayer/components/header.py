import reflex as rx

def header():
    return rx.box(
        rx.hstack(
            rx.icon("menu"),
            rx.spacer(),
            rx.icon("bell"),
            rx.icon("users"),
            rx.icon("user"),
            spacing="4",
            margin_left="20px"
        ),
        height="64px",
        margin_top="2vh"
    )