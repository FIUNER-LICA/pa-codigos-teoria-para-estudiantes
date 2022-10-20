# -*- coding: utf-8 -*-
"""
Ejemplos con mutaciones
"""

import numpy as np

# ------------------------------------
# Reformar (reshape) un np.array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

nuevo_arr_1 = arr.reshape(2, 6) # 1D a 2D
nuevo_arr_2 = arr.reshape(3, 4) # 1D a 2D
nuevo_arr_3 = arr.reshape(4, 3) # 1D a 2D
nuevo_arr_4 = arr.reshape(3, 2, 2) # 1D a 3D
nuevo_arr_5 = nuevo_arr_4.reshape(-1)
nuevo_arr_6 = nuevo_arr_4.ravel()

print(nuevo_arr_1)
print(nuevo_arr_2)
print(nuevo_arr_3)
print(nuevo_arr_4)
print(nuevo_arr_5)
print(nuevo_arr_6)

print()

# ------------------------------------
# Iterar en un np.array y modificar su contenido
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr.shape)
print(arr)

for arr_dim_2 in arr:
    print(arr_dim_2)
    
for arr_dim_2 in arr:
    for arr_dim_3 in arr_dim_2:
        for elem in arr_dim_3:
            print(elem)

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        for k in range(arr.shape[2]):
            arr[i,j,k] += 3

print(arr)
