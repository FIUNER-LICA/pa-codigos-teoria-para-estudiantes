# -*- coding: utf-8 -*-

import timeit

def factorial_rec(n):
    res = 1
    for i in range(1,n+1):
        res = i*res
    return res

def invocable_1():
    global f5
    f5 = factorial_rec(5)
    
def invocable_2():
    global f50
    f50 = factorial_rec(50)

def invocable_3():
    global f500
    f500 = factorial_rec(500)

# Notar que aunque n se multiplica por 10 cada vez, el tiempo requerido se multiplica por un factor mayor
tiempo1 = timeit.timeit(invocable_1, number=1000)
tiempo2 = timeit.timeit(invocable_2, number=1000)
tiempo3 = timeit.timeit(invocable_3, number=1000)

print(f"factorial_rec(5), {tiempo1}: {f5}")
print(f"factorial_rec(50), {tiempo2}: {f50}")
print(f"factorial_rec(500), {tiempo3}: {f500}")
