# aqui se colocan los metodos que interactuan con nuestra base de datos 
from ..model.permisos_navegacion import Navegacion
from .connect_db import connect
from sqlmodel import Session, select
from sqlmodel import Session, select

def select_user_navegacion(email: str):
    engine = connect()
    with Session(engine) as session:
        query = select(Navegacion.calidad).where(Navegacion.email == email)
        result = session.exec(query).fetchall()
        print (result)
        if result:
            return [{'calidad': row[0]} for row in result]
        else:
            return None 