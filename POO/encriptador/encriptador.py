class Encriptador:
    cantidad_de_objetos = 0

    def __init__(self, p_nueva_clave = "1234567890"):
        # self.__clave = p_nueva_clave  # mejor no
        
        self.__clave = None
        self.set_clave(p_nueva_clave)

        self.__algoritmo_de_encirptacion = "sustitución"

        Encriptador.cantidad_de_objetos += 1

        # ejemplo
        # self.atributo_publico = 1
        # self.__atributo_privado = "hola"

    def __del__(self):
        Encriptador.cantidad_de_objetos -= 1

    def set_clave(self, p_nueva_clave):
        if not isinstance(p_nueva_clave, str):
            raise Exception("La clave debe ser de tipo string")
        if len(p_nueva_clave) < 10:
            raise Exception("La clave tiene menos de 10 caracteres.")
        self.__clave = p_nueva_clave
            
        # if isinstance(p_nueva_clave, str):
        #     if len(p_nueva_clave) >= 10:
        #         self.__clave = p_nueva_clave
        #     else:
        #         raise Exception("La clave tiene menos de 10 caracteres.")
        # else:
        #     raise Exception("La clave debe ser de tipo string")

    def get_clave(self):
        return self.__clave  
    
    # inicio pripiedad clave
    # getter
    @property
    def clave(self):
        print("se invoca la propiedad getter clave")
        return self.__clave

    @clave.setter
    def clave(self, p_nueva_clave):
        self.set_clave(p_nueva_clave)
    # fin propiedad clave

    def encriptar(self, p_mensaje):
        # controles sobre los parámetros
        mensaje_encriptado = ""
        for caracter in p_mensaje:
            mensaje_encriptado += chr(ord(caracter)+1)
        return mensaje_encriptado

    def desencriptar(self, p_mensaje_encriptado):
        # controles sobre los parámetros
        mensaje_desencriptado = ""
        for caracter in p_mensaje_encriptado:
            mensaje_desencriptado += chr(ord(caracter)-1)
        return mensaje_desencriptado

    def devolver_mi_identidad(self):
        return hex(id(self))
    
    def __metodo_privdo(self):
        pass

    def __str__(self):
        return f"Encriptador (algoritmo: {self.__algoritmo_de_encirptacion})"