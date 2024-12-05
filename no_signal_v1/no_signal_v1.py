import reflex as rx
from components.navbar import navbar
from components.header import header
from components.link import link
from rxconfig import config

import no_signal_v1.styles.styles as styles
from no_signal_v1.styles.styles import Size

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            header(),
            link(),
            align="center",
            width="100%",
        ),
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    html_lang='es'
)
app.add_page(index)
