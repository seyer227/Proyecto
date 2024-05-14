# aqui se colocan los metodos que interactuan con nuestra base de datos 
from ..model.permisos_navegacion import Permisos
from .connect_db import connect
from sqlmodel import Session, select
from sqlmodel import Session, select

def select_user_navegacion(email: str):
    engine = connect()
    with Session(engine) as session:
        query = select(Permisos).where(Permisos.email == email)
        result = session.exec(query).one_or_none()
        print (result)
        return result