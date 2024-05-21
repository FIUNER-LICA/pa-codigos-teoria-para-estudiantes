from sqlalchemy import create_engine

def crear_engine():
    engine = create_engine("sqlite:///POO/desacople/datos/base_de_datos.db")
    return engine
