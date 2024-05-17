# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:31:09 2022

@author: jordan
"""

# Ejemplo 7:
    
class Individuo:
    def __init__(self, codigo): 
        self.__codigo = codigo
    
    def __str__(self): 
        return "Individuo: " + self.__codigo
        
class Poblacion:
    def __init__(self):
        self.__individuos = [Individuo('A'), Individuo('B'), Individuo('C')]
        
    def __iter__(self):
        return (x for x in self.__individuos)


poblacion = Poblacion()

for individuo in poblacion:
    print(individuo)