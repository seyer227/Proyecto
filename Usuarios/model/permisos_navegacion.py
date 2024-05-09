import reflex as rx 
from typing import Optional
from sqlmodel import Field

class Navegacion (rx.Model,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    Usuario:str
    calidad: str
    usuarios: str
    email:str
# si neceistamos mas tablas o tenemos mas tablas que queremos mostrar debemos agrgar mas modelos a la carpeta con esta estructura similar 
