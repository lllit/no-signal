import reflex as rx
from components.navbar import navbar
from components.header import header
from components.link import link
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                link(),
                align_items="center",
                max_width="620px"
            ),
        ),
    )


app = rx.App()
app.add_page(index)
