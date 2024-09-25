import reflex as rx
from components.title import title
from components.link_button import link_button
def link() -> rx.Component:
    return rx.vstack(
        link_button(
            title="Produccion musical con Ableton Live",
            body="Nivel Inicial / Nivel Avanzado",
            image="/ico-1.png",
            url="#",
            color="#3661f2",
            color_text="#bdabf3",
        ),
        link_button(
            title="DJ house, minimal, Deep, tech house",
            body="Nivel Inicial / Nivel Avanzado",
            image="/ico-2.png",
            url="#",
            color="#888989",
            color_text="#def67c",
        ),
        link_button(
            title="DJ techno, trance, up tempo",
            body="Nivel Inicial / Nivel Avanzado",
            image="/ico-3.png",
            url="#",
            color="#caed6f",
            color_text="#3f4933",
        ),
        link_button(
            title="Tornamesismo",
            body="Nivel Inicial / Nivel Avanzado",
            image="/ico-4.png",
            url="#",
            color="#bdabf3",
            color_text="#d8522b",
        ),
        link_button(
            title="DJ freestye, hip-hop, funky",
            body="Nivel Inicial / Nivel Avanzado",
            image="/ico-5.png",
            url="#",
            color="#d8522b",
            color_text="#e1a6a4",
        ),
        align="center",
        spacing="4",
        width="100%"
    )