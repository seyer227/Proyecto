import reflex as rx 
from ..model.calidad_model import AlertasCalidad
from ..service.calidad_service import select_all_calidad,select_calidad_articulo_service
from ..routes import Route
from Usuarios.components.navbar import navbar

class AlertasState(rx.State):
    # states
    alerta:list[AlertasCalidad]
    alerta_buscar : str
    
    @rx.background
    async def get_all_alertas(self):
        async with self:
            self.alerta = select_all_calidad()
            
    @rx.background
    async def get_calidad_articulo (self):
        async with self :
            self.alerta = select_calidad_articulo_service(self.alerta_buscar)
    def buscar_on_change(self,value:str):
        self.alerta_buscar=value

@rx.page(route=Route.CALIDAD.value,title='Calidad',on_load=AlertasState.get_all_alertas)
def alerta_page() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.flex(
            rx.heading('Alertas de Calidad',align='center',color= 'white'),
            rx.hstack(
                buscar_articulo_component(),
                justify='end',
                style={'margin top':'40px'}
            ),        
            table_calidad(AlertasState.alerta),
            direction='column',
            style={"width":"60vw","margin":"auto"}
        ),
        )


def table_calidad(list_calidad:list[AlertasCalidad])->rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('Articulo'),
                rx.table.column_header_cell('Prensa'),
                rx.table.column_header_cell('Motivo'),
            )
        ),
        rx.table.body(
            rx.foreach(list_calidad,row_table)
        )
        
    )

def row_table(alerta:AlertasCalidad)->rx.Component:
    return rx.table.row(
        rx.table.cell(alerta.CodArticolo),
        rx.table.cell(alerta.RisorseAvvisoQualita),
        rx.table.cell(alerta.MotivazioneAvvisoQualita),
        rx.table.cell(rx.hstack(
            rx.button('eliminar')
        )
        )
        
    )    
    

def buscar_articulo_component()-> rx. Component:
    return rx.stack(
        rx.input(placeholder='Ingrese acticulo',on_change=AlertasState.buscar_on_change),
        rx.button('Buscar Articulo', on_click=AlertasState.get_calidad_articulo)
    )