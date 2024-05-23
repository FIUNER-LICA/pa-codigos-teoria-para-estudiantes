# -*- coding: utf-8 -*-

def busqueda_binaria(unaLista, item):
    primero = 0
    ultimo = len(unaLista)-1
    encontrado = False

    while primero<=ultimo and not encontrado:
        puntoMedio = (primero + ultimo)//2
        if unaLista[puntoMedio] == item:
            encontrado = True
        else:
            if item < unaLista[puntoMedio]:
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1

    return encontrado


listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(busqueda_binaria(listaPrueba, 3))
print(busqueda_binaria(listaPrueba, 13))