from ..repository.navegacion_repository import select_user_navegacion
import reflex as rx

#Acceso al portal
def select_user_navegacion_service(email: str):
    if len(email) != 0:
        navegacion = select_user_navegacion(email)
        if navegacion:
            print('acceso a navegar')
            return {'calidad':navegacion.calidad,'usuarios':navegacion.usuarios,'calendario':navegacion.calendario}
        else:
            print('Error: usuario sin permiso de navegacion, si requieres el acceso comunicate con el area de sistemas')
            raise BaseException('Error: usuario sin permiso de navegacion, si requieres el acceso comunicate con el area de sistemas')