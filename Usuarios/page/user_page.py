import reflex as rx 
import asyncio
from ..model.user_model import User
from ..service.user_service import select_all_user_service,select_user_by_email_service,create_user_service,delete_user_service
from ..notify import notify_component
from ..routes import Route
from Usuarios.components.navbar import navbar

class UserState(rx.State):
    #states
    users:list[User]
    user_buscar:str
    error:str=''
    
    @rx.background
    async def crea_user(self,data : dict):
        async with self:
            try:
                self.users = create_user_service(username=data['username'],password=data['password'],name=data['name'],phone=data['phone'])
            except BaseException as be:
                print(be.args)
                self.error = be.args
        await self.handleNotify()
    
    
    # esto trae todos los datos a la pantalla de la web es decir la informacion de la tabla
    @rx.background
    async def get_all_user(self):
        async with self:
            self.users = select_all_user_service()
    
    #busqueda por usuario
    @rx. background
    async def get_user_by_email(self):
        async with self:
            self.users = select_user_by_email_service(self.user_buscar)
    
    async def handleNotify(self): # esto es un componente
        async with self: 
            await asyncio.sleep(2)
            self.error=''
    
    def buscar_on_change(self,value:str):
        self.user_buscar=value
        
    @rx. background
    async def delete_user_by_email(self,email):
        async with self:
            self.users = delete_user_service(email)


# creacion de la pagina y su configuracion 
@rx.page(route=Route.USER.value,title='user', on_load=UserState.get_all_user)
def user_page()-> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.flex(
            rx.heading('Usuarios',align='center'),
            rx.hstack(
                buscar_user_component(),
                create_user_dialogo_component(),
                administrar_navegacion(),
                justify='end',
                style={'margin-top':'30px'}
            ),
            table_user(UserState.users),
            rx.cond(
                UserState.error != '',
                notify_component(UserState.error,'shield-alert','yellow')
            ),
            direction= 'column',
            style = {"width":"60vw","margin":"auto"}
        )
    )
# es la creacion de la taba 
def table_user(list_user:list[User])->rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('Nombre'),
                rx.table.column_header_cell('Email'),
                rx.table.column_header_cell('Telefono'),
                rx.table.column_header_cell('Accion')
            )
        ),
        rx.table.body(
            rx.foreach(list_user,row_table) #
        )
    )
# son las filas de las tablas 
def row_table(user:User)-> rx.Component:
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.username),
        rx.table.cell(user.phone),
        rx.table.cell(rx.hstack(
            delete_user_dialogo_component(user.username)
        ))
    )


def administrar_navegacion () -> rx.Component:
    return rx.hstack(
        rx.chakra.link(
            rx.button("Example"),
            href=Route.ADMINISTRADORNAVEGACION.value,
        )
    )

# creo el boton de buscar usuario 
def buscar_user_component()-> rx.Component:
    return rx.hstack(
        rx.input(placeholder='Ingrese email', on_change=UserState.buscar_on_change),
        rx.button('Buscar usuario', on_click=UserState.get_user_by_email)
    )
#Creo el formulario para agregar usuarios
def create_user_form()->rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder='Nombre',
                name= "name",
            ),
            rx.input(
                placeholder= 'Email',
                name="username"
            ),
            rx.input(
                placeholder='Contraseña',
                name="password",
                type='password'  
            ),
            rx.input(
                placeholder='Telefono',
                name="phone"
            ),
            rx.dialog.close(
                rx.button('Guardar',type='submit')
            ),
        ),
        on_submit=UserState.crea_user,
    )


#dialogo es una ventana emergente que solicita la informacion para agregar un usuario
def create_user_dialogo_component()-> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button('Crear usuario')),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title('Crear usuario'),
                create_user_form(),
                justify='center',
                align='center',
                direction='column',
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button('Cancelar',color_scheme='gray', variant= 'soft')
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            style={'width':'300px'}
        ),
    )

#Creacion de dialogo para confirmar la eliminacion del registro de usu
def delete_user_dialogo_component(username:str)->rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon('trash-2'))),
        rx.dialog.content(
            rx.dialog.title('Eliminar usuario'),
            rx.dialog.description('Está seguro de querer eliminar el usuario:  ' + username),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        'Cancelar',
                        color_scheme='gray',
                        variant='soft'
                    ),
                ),
                rx.dialog.close(
                    rx.button('Confirmar',on_click=UserState.delete_user_by_email(username)),
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            )
            
        )
    )