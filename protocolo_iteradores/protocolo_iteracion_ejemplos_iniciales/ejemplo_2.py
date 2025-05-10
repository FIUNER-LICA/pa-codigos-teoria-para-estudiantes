# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:00:35 2022

@author: jordan
"""

# Ejemplo 2:
    
print()
iterador1 = iter([1, 2, 3, 4])
for x in iterador1: print(x ** 2, end=' ')

print()
iterador2 = iter((1, 2, 3, 4))
for x in iterador2: print(x ** 3, end=' ')

print()
iterador3 = iter('abcd')
for x in iterador3: print(x * 2, end=' ')

print()
print(iterador1)
print(iterador2)
print(iterador3)

