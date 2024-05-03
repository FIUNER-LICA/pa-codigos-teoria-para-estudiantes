# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:35:12 2022

@author: jordan
"""

# Ejemplo 5:

lista = [1, 2, 3, 4]
archivo = open('comidas.txt')

# la lista retorna otro objeto
iterador_1 = iter(lista)
# el archivo se retorna a sí mismo
iterador_2 = iter(archivo)

print(iterador_1 is lista)
print(iterador_2 is archivo)

print()
print(id(lista))
print(id(iterador_1))
print(id(archivo))
print(id(iterador_2))

