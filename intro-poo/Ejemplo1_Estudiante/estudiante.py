# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:30:23 2023

@author: jfi
@author: dz
Ejemplo de una clase simple
"""

# se define la clase que modela UN estudiante
class Estudiante:
    # se invoca en la construcción de 
    # un objeto
    def __init__(self):
        self._nombre = "S/N"
        self.__carrera = "vacio"

    def set_nombre(self, p_nombre):
        self._nombre = p_nombre

    def get_nombre(self):
        return self._nombre
    
    # uso de decoradores
    @property
    def carrera(self):
        print("Soy el getter del atributo __carrera")
        return self.__carrera
    
    @carrera.setter
    def carrera(self, p_carrera):
        print("Soy el setter del atributo __carrera")
        if p_carrera != "":
            self.__carrera = p_carrera
        else:
            raise Exception("La carrera no puede estar vacía")

    # se le enseña a la clase a 
    # convertirse a una cadena de 
    # caracteres (string)
    def __str__(self):
        cad = self._nombre
        cad += ", " + self.__carrera
        return cad

un_estudiante = Estudiante()
otro_estudiante = Estudiante()

# en la siguiente línea self hace 
# referencia al objeto un_estudiante
un_estudiante.set_nombre("Aixa")

# en la siguiente línea self hace 
# referencia al objeto otro_estudiante
otro_estudiante.set_nombre("Juan")

# Acceso NO recomendado a atributos privados
# otro_estudiante._Estudiante__carrera = "Lic. en Bioinformática"

# print(un_estudiante)
# print(otro_estudiante)

# # se accede directamente al atributo del objeto
# otro_estudiante._nombre = "Juan Manuel"
# otro_estudiante.carrera = "Lic. en Bioinformática"
# print("Carrera del otro_estudiante:", 
#       otro_estudiante.carrera)

print(otro_estudiante)
otro_estudiante.carrera = "" # se lanza una excepcion



















