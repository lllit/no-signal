import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.image(src="/icon1.png", width ="90px",padding_top="20px"),
        rx.hstack(
            rx.icon("headphones"),
            rx.text("_ACADEMY"),
            padding="20px",
        ),
        align="center",
        background="transparent",
        border_bottom="1px solid #fff5",
        border_radius = "30px",
        box_shadow= "0px 10px 15px -25px #fff",
        min_width="90vw",
        padding_bottom= "10px",
        margin_bottom="10px"
    )
