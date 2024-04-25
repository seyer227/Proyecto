import reflex as rx
import Proyecto.styles.styles as styles
from Proyecto.pages.AlertaCalidad import alerta_page


class State (rx.State):
    """Define your app state here."""

app = rx.App(
    stylesheets=styles.STYLESHEETS, 
    style=styles.BASE_STYLE
)
