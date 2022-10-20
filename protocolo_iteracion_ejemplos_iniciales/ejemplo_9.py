# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:37:59 2022

@author: jordan
"""

# Ejemplo 9:
    
class Individuo:
    def __init__(self, codigo): 
        self.codigo = codigo
    def __str__(self): 
        return "Individuo: " + self.codigo
        
class Poblacion(list):
    def __init__(self):
        self.individuos = [Individuo('A'), Individuo('B'), Individuo('C')]  
    def __iter__(self):
        for x in self.individuos:
            yield x

poblacion = Poblacion()

iterador = iter(poblacion)

print(iterador)
print(next(iterador))
print(next(iterador))
print(next(iterador))
# print(next(iterador))  # excepción StopIteration
