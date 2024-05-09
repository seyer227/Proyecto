from ..model.calidad_model import AlertasCalidad
from .connect_db_calidad import connect
from sqlmodel import Session,select


def select_all_calidad():
    engine = connect()
    with Session (engine) as session:
        query = select(AlertasCalidad)
        return session.exec(query).all()
    

def select_calidad_articulo(Articolo: str):
    engine = connect()
    with Session(engine) as session:
        query = select(AlertasCalidad).where(AlertasCalidad.CodArticolo == Articolo)
        return session.exec(query).all()
    