# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:10:29 2022

@author: jordan
"""

# Ejemplo 3:
    
lista = [1, 2, 3]

iterador_1 = iter(lista)
for x in iterador_1: print(x ** 2, end=' ')

print()
iterador_2 = iter(lista)
x = next(iterador_2) # ó: iterador_2.__next__()
print(x ** 2, end=' ')
x = next(iterador_2)
print(x ** 2, end=' ')
x = next(iterador_2)
print(x ** 2, end=' ')

print()
print(iterador_1)
print(iterador_2)

# se alza excepción StopIteration
x = next(iterador_2)    



