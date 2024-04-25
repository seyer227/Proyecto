from ..repository.user_repository import select_all,select_calidad_articulo



def select_all_user_service():
    alertascalidad = select_all
    print (alertascalidad)
    return alertascalidad

def select_calidad_articulo_service(Articolo: str):
    if (len(Articolo) !=0):
        return select_calidad_articulo(Articolo)
    else: 
        return select_all()
    