# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:31:09 2022

@author: jordan
"""

# Ejemplo 7:
    
class Individuo:
    def __init__(self, codigo): 
        self.codigo = codigo
    
    def __str__(self): 
        return "Individuo: " + self.codigo
        
class Poblacion:
    def __init__(self):
        self.individuos = [Individuo('A'), Individuo('B'), Individuo('C')]
        
    def __iter__(self):
        return (x for x in self.individuos)


poblacion = Poblacion()

for individuo in poblacion:
    print(individuo)