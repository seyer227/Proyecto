import reflex as rx
import Usuarios.styles.styles as styles
from Usuarios.styles.styles import Size
from Usuarios.styles.colors import Color
from Usuarios.routes import Route
from Usuarios.page.Login import LoginState

def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.link(
            rx.chakra.box(
                rx.chakra.span("Ext", color=Color.PRIMARY.value,),
                rx.chakra.span("met", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href=Route.MENU.value
        ),
        rx.flex(
            rx.hstack(
                rx.text(LoginState.logged_user, weight="bold", size="2"),
                rx.spacer(size="1"),
                align_items="center"
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("Options", variant="soft"),
                ),
                rx.menu.content(
                    rx.menu.item("Edit"), #shortcut="⌘ E"),
                    rx.menu.item("Duplicate"),
                    rx.menu.separator(),
                    rx.menu.item("Archive",),
                    rx.menu.sub(
                        rx.menu.sub_trigger("More"),
                        rx.menu.sub_content(
                            rx.menu.item("Move to project…"),
                            rx.menu.item("Move to folder…"),
                            rx.menu.separator(),
                            rx.menu.item("Advanced options…"),
                        ),
                    ),
                    rx.menu.separator(),
                    rx.menu.item("Share"),
                    rx.menu.item("Add to favorites"),
                    rx.menu.separator(),
                    rx.menu.item(rx.chakra.link("Cerrar Sesión", color="red",href=Route.INDEX.value)),
                ),
            ),
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        justify_content="space-between"  # Añadido para mover el botón a la derecha
    )

