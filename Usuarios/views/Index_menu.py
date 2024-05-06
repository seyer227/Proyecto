import reflex as rx
from Usuarios.routes import Route
from Usuarios.components.link_button import link_button
from Usuarios.components.title import title
from Usuarios.styles.styles import Size


def index_links() -> rx.Component:
    return rx.chakra.vstack(
        title("Navegacion a modulos"),
        rx.chakra.hstack(
        link_button(
            "Usuarios",
            "Alta y Baja de Usuarios",
            "/icons/user-solid.svg",
            Route.USER.value,
            is_external=False,
        ),
        link_button(
            "Usuarios",
            "Alta y Baja de Usuarios",
            "/icons/user-solid.svg",
            Route.USER.value,
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
