from sqlalchemy import create_engine

URL_BD = "sqlite:///POO/desacople/datos/base_de_datos.db"

def crear_engine():
    engine = create_engine(URL_BD)
    return engine
