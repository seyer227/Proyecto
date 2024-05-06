import reflex as rx
import Usuarios.styles.styles as styles
from Usuarios.components.navbar import navbar
from Usuarios.views.Index_menu import index_links
from Usuarios.styles.styles import Size
from ..routes import Route



@rx.page(route=Route.MENU.value, title='Menu')
def Menu_page() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.box(
            rx.chakra.hstack(
                index_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.ZERO.value,
                padding=Size.BIG.value,
            ),
        ),
        
    )