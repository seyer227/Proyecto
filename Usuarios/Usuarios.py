import reflex as rx
import Usuarios.styles.styles as styles
from Usuarios.page.user_page import user_page
from Usuarios.page.Menu import Menu_page
from Usuarios.page.Login import login_page
from Usuarios.page.AlertaCalidad import alerta_page
from Usuarios.page.calendar import calendario

class State (rx.State):
    """Define your app state here."""

app = rx.App(
    stylesheets=styles.STYLESHEETS, 
    style=styles.BASE_STYLE
)
