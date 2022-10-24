# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:33:28 2022

@author: jorda
"""
import numpy as np

n = 50

R = np.zeros(n, dtype=[
    ("position", float, (2,)),
    ("size", float, (1,)), 
    ("color", float, (4,)) 
    ])

R["position"] = np.random.uniform(0, 1, (n,2))
R["size"] = np.linspace(0, 1, n).reshape(n,1)
R["color"][:,3] = np.linspace(0, 1, n)

print(R)

print(R.shape) # cantidad de filas
print(R["size"].shape) # cantidad de filas
print(np.linspace(0, 1, n).shape)

print(R["position"][24])
print(R["position"][24, 1])
print(R["size"][24])
print(R["size"][24, 0])
print(R["color"][24])




