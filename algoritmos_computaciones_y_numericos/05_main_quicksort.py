# -*- coding: utf-8 -*-
"""
Basado en http://137.184.129.83/ns/books/published/pythoned/SortSearch/ElOrdenamientoRapido.html
"""

def ordenamiento_rapido(unaLista):
   __ordenamiento_rapido_auxiliar(unaLista,0,len(unaLista)-1)

def __ordenamiento_rapido_auxiliar(unaLista,primero,ultimo):
   if primero<ultimo:
       puntoDivision = __particion(unaLista,primero,ultimo)
       __ordenamiento_rapido_auxiliar(unaLista,primero,puntoDivision-1)
       __ordenamiento_rapido_auxiliar(unaLista,puntoDivision+1,ultimo)

def __particion(unaLista,primero,ultimo):
   valorPivote = unaLista[primero]
   marcaIzq = primero+1
   marcaDer = ultimo
   hecho = False
   while not hecho:
       while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1
       while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1
       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = unaLista[marcaIzq]
           unaLista[marcaIzq] = unaLista[marcaDer]
           unaLista[marcaDer] = temp
   temp = unaLista[primero]
   unaLista[primero] = unaLista[marcaDer]
   unaLista[marcaDer] = temp
   return marcaDer

unaLista = [54,26,93,17,77,31,44,55,20]
ordenamiento_rapido(unaLista)
print(unaLista)
