from modulos.repositorio import Repositorio
from modulos.modelos import ModeloLibro
from modulos.entidades import Libro
from modulos.configuraciones import crear_engine
# Para crear BD y sus tablas inicialmente
from sqlalchemy import MetaData
# Para interactuar con la BD
from sqlalchemy.orm import Session  
from sqlalchemy import select


# Define una implementación concreta para el repositorio. 
# Esto podría ser otra clase que interaccione de otra forma con el sistema de almacenamiento.
class RepositorioSQL(Repositorio):
    def __init__(self) -> None:
        super().__init__()
        # Aquí se creara la BD con sus tablas si no existe.
        self.__engine = crear_engine()
        tabla_libro = ModeloLibro()
        tabla_libro.metadata.create_all(self.__engine) # Crea la tabla utilizando el motor de la BD

    def leer_libro(self, id: int) -> Libro:
        with Session(crear_engine()) as session:
            modelo_libro = session.query(ModeloLibro).filter_by(id=id).first() # Equivale a: modelos_libros = ModeloLibro.query.all()
            
            if modelo_libro is None:
                raise ValueError("No se encuentra un libro con el ID proporcionado")
            
            # Se mapea un ModeloLibro a un Libro           
            libro = self.__convertir_ModeloLibro_a_Libro(modelo_libro)
            
            # Se retorna el Libro
            return libro
        return None

    def guardar_libro(self, libro: Libro) -> None:
        with Session(self.__engine) as session:
            # Buscar si hay un libro con el mismo nombre
            modelo_libro_de_la_BD_con_igual_nombre = session.query(ModeloLibro).filter(ModeloLibro.nombre == libro.get_nombre()).first()
            if modelo_libro_de_la_BD_con_igual_nombre is not None:
                raise ValueError("No puede haber dos libros con el mismo título")
            
            # Buscar si hay al menos un libro en la BD
            modelo_libro_de_la_BD = session.query(ModeloLibro).order_by(ModeloLibro.id.desc()).first() # Se accede al regitro con mayor ID
            if modelo_libro_de_la_BD is not None:
                # Si lo hay, entonces, se debe tomar un ID igual al último de la tabla y sumarle 1
                libro.set_id(modelo_libro_de_la_BD.id + 1)
            else:
                # Caso contrario, establecer el id a 1.
                libro.set_id(1)

            # Se mapea un Libro a un ModeloLibro
            modelo_libro = self.__convertir_Libro_a_ModeloLibro(libro)

            # Se almacena el ModeloLibro
            session.add(modelo_libro)
            session.commit()
    
    def actualizar_libro(self, libro: Libro) -> None:
        with Session(self.__engine) as session:
            # Buscar si hay un libro con el mismo id del libro
            modelo_libro = session.query(ModeloLibro).filter(ModeloLibro.id == libro.get_id()).first()
            if modelo_libro is None:
                raise ValueError("No se encuentra un libro con este ID.")
            
            # Se mapea un Libro a un ModeloLibro
            modelo_libro = self.__convertir_Libro_a_ModeloLibro(libro)

            # Se almacena el ModeloLibro
            session.query(ModeloLibro).filter(ModeloLibro.id == libro.get_id()).update({
                "nombre": modelo_libro.nombre,
                "autor": modelo_libro.autor,
                "calificacion": modelo_libro.calificacion
            })
            session.commit()
    
    def borrar_libro(self, libro: Libro):
        with Session(self.__engine) as session:
            # Buscar si hay un libro con el mismo id del libro
            modelo_libro = session.query(ModeloLibro).filter(ModeloLibro.id == libro.get_id()).first()
            if modelo_libro is None:
                raise ValueError("No se encuentra un libro con este ID.")
            
            # Se borra el libro de la BD
            session.query(ModeloLibro).filter(ModeloLibro.id == libro.get_id()).delete(synchronize_session=False)
            session.commit()

    def get_lista_libros(self):
        lista_de_libros = []
        # levantar todos los libros de la BD
        with Session(crear_engine()) as session:
            modelos_libros = session.query(ModeloLibro).all() # Equivale a: modelos_libros = ModeloLibro.query.all()
            ml = modelos_libros[0]
            for modelo_libro in modelos_libros:        
                # convertir cada objeto ModeloLibro en Libro
                libro = self.__convertir_ModeloLibro_a_Libro(modelo_libro)
                # añadir cada libro a la lista de libros
                lista_de_libros.append(libro)

        return lista_de_libros
    
    def __convertir_Libro_a_ModeloLibro(self, libro: Libro) -> ModeloLibro:
        modelo_libro = ModeloLibro()
        modelo_libro.id = libro.get_id()
        modelo_libro.nombre = libro.get_nombre()
        modelo_libro.autor = libro.get_autor()
        modelo_libro.calificacion = libro.get_puntaje()
        return modelo_libro
    
    def __convertir_ModeloLibro_a_Libro(self, modelo_libro: ModeloLibro) -> Libro:
        id = int(modelo_libro.id)
        nombre = str(modelo_libro.nombre)
        autor = str(modelo_libro.autor)
        puntaje = float(modelo_libro.calificacion)
        libro = Libro(id, nombre, autor, puntaje)
        return libro
        
        
class RepositorioCSV(Repositorio):
    pass