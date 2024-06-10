from POO.encriptador.encriptador import Encriptador


encriptador_1 = Encriptador()

print("encriptador_1:", encriptador_1)

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
print("identidad del objeto 2:", hex(id(encriptador_2)))
print("identidad del objeto 2:", encriptador_2.devolver_mi_identidad())

mensaje = "hola y bienvenidos"
mensaje_encriptado = encriptador_1.encriptar(mensaje)
print("mensaje_encriptado:", mensaje_encriptado)
mensaje_desencriptado = encriptador_1.desencriptar(mensaje_encriptado)
print("mensaje_desencriptado:", mensaje_desencriptado)

# encriptador_2.clave = "otra clave re dificil"
# print(encriptador_2.clave)

# # Atributo de clase
# print("Encriptador.cantidad_de_objetos:", Encriptador.cantidad_de_objetos)


# Ejemplo con atributos de clase:
encriptadores = [Encriptador() for _ in range(10)] # se crean encriptadores adicionales (en una lista)

print("Encriptador.cantidad_de_objetos:", Encriptador.cantidad_de_objetos)

# se borran dos encriptadores (los que no estaban en la lista)
del encriptador_1
del encriptador_2

print("Encriptador.cantidad_de_objetos:", Encriptador.cantidad_de_objetos)
