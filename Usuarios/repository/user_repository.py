# aqui se colocan los metodos que interactuan con nuestra base de datos 
from ..model.user_model import User
from .connect_db import connect
from sqlmodel import Session, select


def select_all_usuarios():
    engine = connect ()
    with Session (engine) as session: #session en minuscula es un alias
        query = select(User) # select * from user 
        return session.exec(query).all()# devuelve una lista 

def select_user_by_email(email : str):
    engine = connect()
    with Session(engine) as session:
        query = select(User).where(User.username==email)
        return session.exec(query).all()
# select * from User wher username = email

#aqui etoy creando el metodo para agregar un usuario pero a su vez regreso y muestro la lista actualizada
def create_user(user:User):
        engine = connect()
        with Session (engine) as session:
                session.add(user)
                session.commit()
                query = select(User)
                return session.exec (query).all()

def delete_user(email:str):
    engine = connect()
    with Session (engine) as session:
        query=select(User).where(User.username == email)
        user_delete = session.exec(query).one()
        session.delete(user_delete)
        session.commit()
        query = select(User)
        return session.exec (query).all()


def select_user_login(email: str, password: str,):
    engine = connect()
    with Session(engine) as session:
        query = select(User.username, User.password,User.name).where(User.username == email, User.password == password)
        result = session.exec(query).fetchall()
        print (result)
        if result:
            return [{'username': row[0], 'password': row[1],} for row in result]
        else:
            return None  # O cualquier otro indicador de que no se encontraron coincidencias

