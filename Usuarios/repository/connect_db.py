from sqlalchemy.engine import URL
from sqlmodel import create_engine

connection_string = "DRIVER={SQL Server Native Client 11.0};SERVER=192.168.10.7,1433;DATABASE=Catalogo_usuarios;UID=pmejia;PWD=EXT3H$lTe8seiv"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

def connect():
    engine = create_engine(connection_url)
    return engine