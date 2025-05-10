# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:10:31 2022

@author: jordan
"""

# Ejemplo 6:

rango = range(3)
enumeracion = enumerate('pyt')

print(rango)
print(enumeracion)

iter1 = iter(rango)
iter2 = iter(enumeracion)

print(iter1)
print(iter2)

print(next(iter1))  # el valor 0 se genera ahora
print(next(iter1))  # el valor 1 se genera ahora
print(next(iter1))  # ...
# print(next(iter1)) # lanza StopIteration

print()
print(next(iter2)) # el valor (0, 'p') se genera ahora
print(next(iter2)) # ...
print(next(iter2)) # ...
# print(next(iter2)) # lanza StopIteration

