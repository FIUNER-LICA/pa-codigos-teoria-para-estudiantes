# -*- coding: utf-8 -*-

def busqueda_binaria(unaLista, item):
    if len(unaLista) == 0:
        return False
    else:
        puntoMedio = len(unaLista)//2
        if unaLista[puntoMedio]==item:
            return True
        else:
            if item<unaLista[puntoMedio]:
                return busqueda_binaria(unaLista[:puntoMedio],item)
            else:
                return busqueda_binaria(unaLista[puntoMedio+1:],item)


listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(busqueda_binaria(listaPrueba, 3))
print(busqueda_binaria(listaPrueba, 13))