import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.flex(
                    rx.avatar(src="/icon1.png"),
                    rx.text(
                        "_ACADEMY",
                        as_="span",
                        color="#fff",
                    ),
                    direction="row",
                    align="center",
                    justify="between",
                    width="100%",
                ),
                display="flex",
            ),
            width="100%",
            href="#",
            is_external=True,
        ),
        position="sticky",
        background="transparent",
        padding_x="2em",
        padding_y="2em",
        top="0"
    ),
