# -*- coding: utf-8 -*-
"""
Ejemplos iniciales
"""

import numpy as np

# ------------------------------------
# Crear un arreglo 1D

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

print(arr.shape)

print()

# ------------------------------------
# Indexar un arreglo

print(arr[0])
print(arr[1])
print(arr[2] + arr[3])
print('Último elemento: ', arr[-1])
print()

# ------------------------------------
# Crear un arreglo 2D

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(arr)

print(type(arr))

print(arr.shape)

print('Elemento de columna 4, fila 2: ', arr[1, 3])
print('Último elemento de segunda fila: ', arr[-1, -1])

print()

# ------------------------------------
# Crear un arreglo 3D de dimensiones 3x2x5

arr = np.array(
    [ # primera dimensión 
     [ # segunda dimensión 
      [1,2,3,4,5],   # tercera dimensión
      [6,7,8,9,10]   # tercera dimensión
     ],
     [ # segunda dimensión
      [11,12,13,14,15],
      [16,17,18,19,20]    # arr[1, 1, 1] == 17
     ],
     [ # segunda dimensión
      [21,22,23,24,25],   # arr[2, 0, 3] == 24
      [26,27,28,29,30]    
     ],
    ])

print(arr)

print(type(arr))

print(arr.shape)

print('Elemento (1,1,1):', arr[1, 1, 1])
print('Elemento (2,0,3):', arr[2, 0, 3])
print('Último elemento de segunda fila, columna y página:', arr[-1, -1, -1])
print(arr[-1,-1,-1] == arr[2,1,4])

print()

# ------------------------------------
# Rebanadas (slicing) de un np.array  [start:end] ó [start:end:step]

arr = np.array(['a', 'b', 'c', 'd', 'e'])

print(arr.dtype)

print(arr[:])
print(arr[:3])
print(arr[2:4])
print(arr[3:])
print(arr[::2])
print(arr[::-2])
print(arr[::-1])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

print()

print(arr.dtype)

print(arr[:])
print(arr[:,:])

print(arr[1,:])
print(arr[1,2:])
print(arr[1:,2:])

print()

# ------------------------------------
# Crear un np.array con un tipo de dato definido
arr = np.array([1, 2, 3, 4, 5], dtype='S')  # string
print(arr.dtype)
print(arr)

arr = np.array([1, 2, 3, 4, 5], dtype='U')  # unicode string
print(arr.dtype)
print(arr)

arr = np.array([1, 2, 3, 4, 5], dtype='f')  # float
print(arr.dtype)
print(arr)

arr = np.array([1, 2, 3, 4, 5], dtype='d')  # double
print(arr.dtype)
print(arr)

print()




