# -*- coding: utf-8 -*-
"""
Ejemplos con número pseudoaleatorios
"""

from numpy import random

# Enteros
arr = random.randint(100, size=(3, 5))

print(arr)

# Reales
arr = random.rand(4)
print(arr)

arr = random.rand(2, 3)
print(arr)

# Elecciones aleatorias
arr = random.choice([i for i in range(20)])
print(arr)
arr = random.choice([i for i in range(20)], size=(3,5))
print(arr)