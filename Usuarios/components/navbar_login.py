import reflex as rx
import Usuarios.styles.styles as styles
from Usuarios.styles.styles import Size
from Usuarios.styles.colors import Color
from Usuarios.routes import Route

def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.link(
        rx.chakra.box(
            rx.chakra.span("Bienvenido a tu portal ", color=Color.PRIMARY.value),
            rx.chakra.span("Extmet", color=Color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        href=Route.INDEX.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
