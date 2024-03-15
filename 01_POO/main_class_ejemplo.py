class Encriptador:
    cantidad_de_objetos = 0

    def __init__(self, p_nueva_clave = "1234567890"):
        # self.__clave = p_nueva_clave  # mejor no
        
        self.__clave = None
        self.set_clave(p_nueva_clave)

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
    

encriptador_1 = Encriptador()

# print("encriptador_1:", encriptador_1)

# print("encriptador_1.atributo_publico:", encriptador_1.atributo_publico)

# print(encriptador_1.get_clave())

# # contrasenia_incorrecta = True
# # while contrasenia_incorrecta:
# try:
#     encriptador_1.set_clave("otraclave")
#     # contrasenia_incorrecta = False
# except Exception as error:
#     print("error:", error)

# print(encriptador_1.get_clave())


# # verificación de indentidad con self
# print("identidad del objeto:", hex(id(encriptador_1)))
# print("identidad del objeto:", encriptador_1.devolver_mi_identidad())

encriptador_2 = Encriptador("una clave re dificil")
# print("identidad del objeto 2:", hex(id(encriptador_2)))
# print("identidad del objeto 2:", encriptador_2.devolver_mi_identidad())

mensaje = "hola y bienvenidos"

mensaje_encriptado = encriptador_1.encriptar(mensaje)

print("mensaje_encriptado:", mensaje_encriptado)

mensaje_desencriptado = encriptador_1.desencriptar(mensaje_encriptado)

print("mensaje_desencriptado:", mensaje_desencriptado)

# print(chr(97))
# print(ord("a"))

encriptador_2.clave = "otra clave re dificil"
print(encriptador_2.clave)

# Atributo de clase
print("Encriptador.cantidad_de_objetos:", Encriptador.cantidad_de_objetos)

encriptadores = [Encriptador() for _ in range(10)]

print("Encriptador.cantidad_de_objetos:", Encriptador.cantidad_de_objetos)

del encriptador_1
del encriptador_2

print("Encriptador.cantidad_de_objetos:", Encriptador.cantidad_de_objetos)
