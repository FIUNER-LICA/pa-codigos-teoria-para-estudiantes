# -*- coding: utf-8 -*-
"""
Basado en http://137.184.129.83/ns/books/published/pythoned/Recursion/LasTorresDeHanoi.html
"""

def moverTorre(altura,origen, destino, intermedio):
    if altura >= 1:
        moverTorre(altura-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(altura-1,intermedio,destino,origen)

def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)

# moverTorre(1,"A","B","C")
# moverTorre(2,"A","B","C")
moverTorre(3,"A","B","C")
