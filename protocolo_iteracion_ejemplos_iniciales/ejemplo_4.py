# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:46:46 2022

@author: jordan
"""

# Ejemplo 4:

print()

lista = [1, 2, 3, 4]

iterador = iter(lista)
while True:
    try:
        x = next(iterador)
    except StopIteration:
        break
    print(x ** 2, end=' ')


print()
for x in lista:
    print(x ** 2, end=' ')
    