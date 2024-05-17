
from sqlalchemy import create_engine
from modulos.repositorio import Repositorio

engine = create_engine('sqlite:///productos.sqlite')

# Define una implementación concreta para el repositorio. 
# Esto podría ser otra clase que interaccione de otra forma con el sistema de almacenamiento.
class RepositorioSQL(Repositorio):
    def leer_libro(id: int) -> Libro:
        # Se mapea un ModeloLibro a un Libro
        
        # Se retorna el Libro
        pass
    
    def guardar_libro(libro: Libro) -> None:
        # Se mapea un Libro a un ModeloLibro
        
        # Se almacena el ModeloLibro
        pass
    
