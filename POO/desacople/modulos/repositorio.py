from abc import ABC, abstractmethod
from modulos.entidades import Libro


# Fija la interfaz de interacción del Modelo de Dominio
class Repositorio(ABC):
    @abstractmethod
    def leer_libro(self, id: int) -> Libro:
        raise NotImplementedError

    @abstractmethod
    def get_lista_libros(self):
        raise NotImplementedError
 
    @abstractmethod
    def guardar_libro(self, libro: Libro) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def actualizar_libro(self, libro: Libro) -> None:
        raise NotImplementedError
   
    @abstractmethod
    def borrar_libro(self, libro: Libro):
        raise NotImplementedError

