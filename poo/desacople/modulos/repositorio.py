from abc import ABC, abstractmethod
from modulos.entidades import Libro

# Fija la interfaz de interacción del Modelo de Dominio
class Repositorio(ABC):
    @abstractmethod
    def leer_libro(id: int) -> Libro:
        raise NotImplementedError
    
    @abstractmethod
    def guardar_libro(libro: Libro) -> None:
        raise NotImplementedError


