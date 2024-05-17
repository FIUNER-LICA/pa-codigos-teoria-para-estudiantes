from modules.config import db
from sqlalchemy import Column, Integer, String, Float

#https://sqlitebrowser.org/dl/
class ModeloLibro(db.Model):
    __tablename__ = 'libros'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False, unique=True)
    autor = Column(String(1000), nullable=False)
    calificacion = Column(Float())
