#sirven la informacion y va la logica es decir aqui hacemos validaciones 
from ..repository.user_repository import select_all_usuarios,select_user_by_email,create_user,delete_user,select_user_login
from ..model.user_model import User
import reflex as rx

def select_all_user_service ():
    users= select_all_usuarios()
    return users

# creacion de metodo 
def select_user_by_email_service(email:str):
    if (len (email)!= 0):
        return select_user_by_email(email)
    else : 
        return select_all_usuarios()
    
#aqui es donde defino y creo como se insertaran los valores de los campos para ingresar un nuevo usuario
def create_user_service(username: str,password:str,phone:str,name:str):
    user= select_user_by_email(username)
    if (len(user)==0):
        user_save= User(username=username,password=password,phone=phone,name=name)
        return create_user(user_save)
    else : 
        print('el usuario ya existe')
        raise BaseException('El usario ya existe')

#eliminacion de usuarios
def delete_user_service(email:str):
    return delete_user(email=email)

#Acceso al portal
def select_user_login_service(email: str, password: str):
    if len(email) != 0 and len(password) != 0:
        user = select_user_login(email, password)
        if user:
            print('Usuario y contraseña correctos')
            return user
        else:
            print('Error: usuario o contraseña inválidos')
            raise BaseException('Error: usuario o contraseña inválidos')
    else:
        print('Error: usuario o contraseña vacíos')
        raise BaseException('Error: usuario o contraseña vacíos')