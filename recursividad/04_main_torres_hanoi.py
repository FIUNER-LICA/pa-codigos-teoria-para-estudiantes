# -*- coding: utf-8 -*-
"""
Basado en http://137.184.129.83/ns/books/published/pythoned/Recursion/LasTorresDeHanoi.html
"""

def mover_torre(altura,origen, destino, intermedio):
    if altura >= 1:
        mover_torre(altura-1,origen,intermedio,destino)
        __mover_disco(origen,destino)
        mover_torre(altura-1,intermedio,destino,origen)

def __mover_disco(desde,hacia):
    print("mover disco de",desde,"a",hacia)

if __name__ == "__main__": 
    mover_torre(3,"A","B","C")
