class MiClase:
    def __init__(self):
        # print("se invoca el método __init__()")
        # print("\tid(self):", hex(id(self)))
        # print()
        self.__un_atributo_entero = 10  # se define un atributo de instancia (o del objeto) 
        una_variable_local_str = "cadena"

    # getter
    def devolverAtributo(self):
        # print(una_variable_local_str)  #error porque es variable local de otro método (el método __init__)
        return self.__un_atributo_entero
    
    # setter
    def modificarAtributo(self, p_nuevo_valor_atributo):
        self.__un_atributo_entero = p_nuevo_valor_atributo



# se crea una instancia (u objeto) de la clase MiClase
un_objeto = MiClase()
otro_objeto = MiClase()

# print("id(un_objeto):", hex(id(un_objeto)))
# print("id(un_objeto):", hex(id(otro_objeto)))
# print()

print("Atributo de un_objeto:", un_objeto.devolverAtributo())
print("Atributo de otro_objeto:", otro_objeto.devolverAtributo())
print()

un_objeto.modificarAtributo(20)

print("Atributo de un_objeto:", un_objeto.devolverAtributo())
print("Atributo de otro_objeto:", otro_objeto.devolverAtributo())
print()

# un_objeto._MiClase__un_atributo_entero = 30  # se puede, pero no se recomienda.

print("Atributo de un_objeto:", un_objeto.devolverAtributo())
print("Atributo de otro_objeto:", otro_objeto.devolverAtributo())
print()


print(type(un_objeto))
print()

a = None

print(a)
print(type(a))