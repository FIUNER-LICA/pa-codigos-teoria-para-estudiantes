# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:34:05 2022

@author: jordan
"""

# Ejemplo 8:
    
class Individuo:
    def __init__(self, codigo): 
        self.codigo = codigo
    
    def __str__(self): 
        return "Individuo: " + self.codigo
        
class Poblacion(list):
    def __init__(self):
        self.__individuos = [Individuo('A'), Individuo('B'), Individuo('C')]
        
    def __iter__(self):
        for x in self.__individuos:
            yield x


poblacion = Poblacion()

for individuo in poblacion:
    print(individuo)