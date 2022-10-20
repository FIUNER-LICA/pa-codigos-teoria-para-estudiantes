# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:35:38 2022

@author: jorda
"""

import numpy as np

n = 5

# Arreglo de numeros
arr1 = np.zeros(n)
print(arr1.dtype)
print(arr1.dtype.names)
print(arr1)
print()

# Arreglo de flotantes de precisión doble
arr2 = np.zeros(n, dtype=[('numeros', np.float64)])  # [0. 0. 0. 0. 0.]
print(arr2.dtype.names)
print(arr2)
print(arr2['numeros'])
print()

arr3 = np.zeros(n,
                dtype=[
                    ('unidades', np.float64),
                    ('decenas', np.int64)
                    ]
                )
print(arr3.dtype.names)
print(arr3)
print(arr3['unidades'])
print(arr3['decenas'])
print(arr3.dtype['unidades'])
print(arr3.dtype['decenas'])
print()

# Generar valores aleatorios uniformes
minimo = -1
maximo = 2
forma = (4,2)
arr4 = np.random.uniform(minimo, maximo, forma)
print(arr4)
print()

# Reformado
N = 8
arr5 = np.linspace(0, 1-1/N, N)
arr6 = arr5.reshape(4,2)
arr7 = arr5.reshape(2,4)
print(arr5)
print(arr6)
print(arr7)
print()

# Pasar de un arreglo matricial a uno lineal
arr8 = np.random.uniform(-5, 5, (3, 2))
arr9 = arr8.ravel()
print(arr8)
print(arr9)
print()

l, m = 2, 5
m, n = 6, 2
A = np.linspace(0, 1-1/(l*m), l*m).reshape(l, m)
B = np.linspace(2, 1-1/(m*n), m*n).reshape(m, n)
R = A @ B
print(A)
print(B)
print(R)
print()