class Libro:
    def __init__(self, p_id, p_nombre, p_autor, p_puntaje):
        self.__id = p_id
        self.__nombre = p_nombre
        self.__autor = p_autor
        self.__puntaje = p_puntaje
    
    # setters
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_autor(self):
        return self.__autor
    def get_puntaje(self):
        return self.__puntaje
    
    # getters
    def set_nombre(self, p_nombre):
        self.__nombre = p_nombre
    def set_autor(self, p_autor):
        self.__autor = p_autor
    def set_puntaje(self, p_puntaje):
        self.__puntaje = p_puntaje
