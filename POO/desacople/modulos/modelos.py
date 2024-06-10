from typing import Any
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase

# declarative base class
class Base(DeclarativeBase):
    pass

#https://sqlitebrowser.org/dl/
class ModeloLibro(Base):        # Base es db.Model en Flask-SQLAlchemy
    __tablename__ = 'libros'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False, unique=True)
    autor = Column(String(1000), nullable=False)
    calificacion = Column(Float())
