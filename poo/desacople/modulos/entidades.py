class Libro:
    def __init__(self, p_id, p_nombre, p_autor, p_puntaje):
        self.__id = p_id
        self.__nombre = None
        self.__autor = None
        self.__puntaje = None
        
        self.set_nombre(p_nombre)
        self.set_autor(p_autor)
        self.set_puntaje(p_puntaje)
    
    # getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_autor(self):
        return self.__autor

    def get_puntaje(self):
        return self.__puntaje
    
    # setters
    def set_id(self, p_id):
        self.__id = p_id

    def set_nombre(self, p_nombre):
        if len(p_nombre.strip()) == 0:
            raise ValueError("El nombre del libro no puede estar en blanco.")
        self.__nombre = p_nombre
    
    def set_autor(self, p_autor):
        if len(p_autor.strip()) == 0:
            raise ValueError("El autor del libro no puede estar en blanco.")
        self.__autor = p_autor
    
    def set_puntaje(self, p_puntaje):
        if not isinstance(p_puntaje, float):
            raise TypeError("El puntaje debe ser un número, y no puede estar en blanco.")
        if not (0.0 <= p_puntaje <= 10.0):
            raise ValueError("El puntaje debe ser un número real entre 0.0 y 10.0.")
        self.__puntaje = p_puntaje
    
    def __str__(self):
        cad = ''
        cad += '"'+self.__nombre+'" - '
        cad += self.__autor
        cad += ' (puntaje: '+str(self.__puntaje)+')'
        return cad