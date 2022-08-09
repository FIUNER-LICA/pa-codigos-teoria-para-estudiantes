# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 12:15:17 2022

@author: dz at fiuner
"""

# Ejemplo de clase que modela un alumno en la FIUNER (o en cualquier facultad).
# Código desarrollado en parte en la pizarra.

class Alumno:
    def __init__(self, p_nom, p_ap, p_carrera):
        self._nom = p_nom
        self._ap = p_ap
        self.carrera = p_carrera 
        
    @property
    def nom(self):
        print("Soy el getter del atributo nom")
        return self._nom
    
    @property
    def ap(self):
        print("Soy el getter del atributo ap")
        return self._ap
    
    @nom.setter
    def nom(self, valor):
        print("Soy el setter de nom")
        if isinstance(valor, str):
            self._nom = valor
        else:
            raise TypeError("El nombre debe ser de tipo string.")
        
    @ap.setter
    def ap(self, valor):
        print("Soy el setter de ap")
        self._ap = valor
        
    def __str__(self):
        return self.nom + " " + self.ap
    
    def imprimir_mi_tipo(self):
        print(type(self))
    
alumno = Alumno("Donald", "Knuth", "Ing. en Transporte")

print(alumno)

alumno.nom = "Donald Ervin"
print()
print(alumno)

# alumno.nom = 1234
# print()
# print(alumno)

print()
print(type(alumno))
print(alumno.imprimir_mi_tipo())



