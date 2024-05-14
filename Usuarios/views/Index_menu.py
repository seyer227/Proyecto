import reflex as rx
from Usuarios.routes import Route
from Usuarios.components.link_button import link_button
from Usuarios.components.title import title
from Usuarios.styles.styles import Size
from ..service.navegacion_service import select_user_navegacion_service
from Usuarios.page.Login import LoginState


def index_links() -> rx.Component:
    return rx.chakra.vstack(
        title("Navegacion a modulos"),
        rx.cond(
            LoginState.show_calidad,  # Condición
            link_button(
            "Calidad",
            "Alertas Calidad",
            "/icons/calidad.svg",
            Route.CALIDAD.value,
            is_external=False,
        ),
        ),
        rx.chakra.hstack(
        rx.cond(
        LoginState.show_usuarios,
        link_button(
            "Usuarios",
            "Alta y Baja de Usuarios",
            "/icons/user-solid.svg",
            Route.USER.value,
            is_external=False,
        ),
        ),
        link_button(
            "CALENDARIO",
            "Registro asistencias",
            "/icons/calendar.svg",
            Route.CALENDARIO.value,
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
