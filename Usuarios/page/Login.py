import reflex as rx
import Usuarios.styles.styles as styles
import asyncio
from ..model.user_model import User
from ..service.user_service import select_user_login_service
from ..notify import notify_component
from ..routes import Route
from Usuarios.styles.styles import Size
from Usuarios.components.navbar_login import navbar
from typing import Optional

class LoginState(rx.State):
    users: list[User]
    user_buscar: str
    password_buscar: str
    error: str = ''

    def reset_fields(self):
        self.user_buscar = ''
        self.password_buscar = ''

    def buscar_user_on_change(self, value: str):
        self.user_buscar = value

    def buscar_password_on_change(self, value: str):
        self.password_buscar = value

    @rx.background
    async def get_user_login(self):
        async with self:
            try: 
                if self.user_buscar and self.password_buscar:
                    self.users = select_user_login_service(self.user_buscar, self.password_buscar)
                    if self.users:
                        # Guardar el nombre de usuario después del inicio de sesión
                        self.save_logged_user(self.users[0]['username'])
                        self.reset_fields()  # Resetear los campos de usuario y contraseña
                        return rx.redirect(Route.MENU.value)
                    else:
                        self.error = 'Error: usuario o contraseña incorrectos'
                        await self.handleNotify()
                else:
                    self.error = 'Error: debe ingresar tanto el usuario como la contraseña'
                    await self.handleNotify()
            except BaseException as be:
                print(be.args)
                self.error = be.args
        await self.handleNotify()

    
    async def handleNotify(self):
        async with self:# esto es un componente 
            await asyncio.sleep(2)
            self.error=''
    
    logged_user: Optional[str] = None  # Variable para almacenar el nombre de usuario después del inicio de sesión

    # Método para guardar el nombre de usuario después del inicio de sesión
    def save_logged_user(self, username: str):
        self.logged_user = username



@rx.page(route=Route.INDEX.value, title='Login')
def login_page() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.flex(
            rx.chakra.heading('Inicio de sesión', align='center', margin_top = Size.VERY_BIG.value),
            rx.chakra.hstack(
                login_user_component(),
            ),
            rx.cond(
                LoginState.error != '',
                notify_component(LoginState.error,'shield-alert','yellow')
            ),
            direction='column',
            style={"width": "60vw", "margin": "auto"},
            align='center',
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin_y=Size.VERY_BIG.value,
            padding=Size.VERY_BIG.value
            
        ),
        
    )

def login_user_component() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder='Ingrese email', on_change=LoginState.buscar_user_on_change),
        rx.input(placeholder='Contraseña', on_change=LoginState.buscar_password_on_change,
                 name="password", type='password'),
        rx.button('Iniciar sesión', on_click=LoginState.get_user_login),
        style={"margin_top": "20px"},
        direction='column',
        align='center'
    )