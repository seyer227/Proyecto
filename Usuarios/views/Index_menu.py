import reflex as rx
from Usuarios.routes import Route
from Usuarios.components.link_button import link_button
from Usuarios.components.title import title
from Usuarios.styles.styles import Size
from ..service.navegacion_service import select_user_navegacion_service
from Usuarios.page.Login import LoginState

x=True
class ToggleState(rx.State):
    show: bool = x  # Variable para controlar la visibilidad

def index_links() -> rx.Component:
    return rx.chakra.vstack(
        title("Navegacion a modulos"),
        rx.cond(
            ToggleState.show,  # Condición
            link_button(
            "Usuarios",
            "Alta y Baja de Usuarios",
            "/icons/user-solid.svg",
            Route.USER.value,
            is_external=False,
        ),
            #rx.text("")  # Se muestra si la condición es False
        ),
        rx.chakra.hstack(
        link_button(
            "Usuarios",
            "Alta y Baja de Usuarios",
            "/icons/user-solid.svg",
            Route.USER.value,
            is_external=False,
        ),
        link_button(
            "Calidad",
            "Alertas calidad",
            "/icons/calidad.svg",
            Route.CALIDAD.value,
            is_external=False,
        ),
        
        width="100%",
        align_items="flex-start",
        spacing=Size.BIG.value,
    ),
        width="100%",
        align_items="flex-start",
        spacing=Size.BIG.value,
    )
