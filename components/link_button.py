import reflex as rx


def link_button(title: str, body: str, image: str, url: str, color: str,color_text:str , is_external=True, animated=False) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.vstack(
                rx.text(
                    body,
                    size="2",
                    color=color_text,
                ),
                rx.text(
                    title,
                    size="5",
                    color=color_text,
                ),
                align_items="start",
                spacing="1",
                padding_y="0.5em",
                padding_right="0.5em"
            ),
            rx.image(
                src=image,
                width="50px",
                heigth="50px",
                alt=title
            ),
            justify="between",
            align="center",
            width="100%"
        ),
        background=color,
        border_radius="10px",
        padding_y="3em",
        padding_x="2em",
        width="100%",
        margin= "5px"
    )
