# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:12:09 2023

@author: jorda
"""

from abc import ABC, abstractmethod

class Instrumento(ABC):
    @abstractmethod
    def ejecutar(self):
        print("ejecutar genérico")  # esto nunca debería ejecutarse

class Afinable(Instrumento):
    pass

class Viento(Instrumento):
    pass

class Guitarra(Afinable):
    def ejecutar(self):
        print("ejecutar nota guitarra")

class Arpa(Afinable):
    def ejecutar(self):
        print("ejecutar nota arpa")

class Flauta(Viento):
    def ejecutar(self):
        c = 4
        # código específico para ejecutar una flauta
        print("ejecutar nota flauta")


class Orquesta:
    def __init__(self) -> None:
        self.__instrumentos = []
    
    def agregar(self, p_instrumento: Instrumento):
        es_instancia_de_una_subcase_de_instrumento = isinstance(p_instrumento, Instrumento)
        no_pertenece_aun = p_instrumento not in self.__instrumentos
        if es_instancia_de_una_subcase_de_instrumento and no_pertenece_aun:
            self.__instrumentos.append(p_instrumento)
        else:
            raise Exception("O no es subclase, o ya pertenece a la orquesta.")

    def ejecutar_obra(self):
        for instrumento in self.__instrumentos:
            instrumento.ejecutar()

    def ejecutar_obra_de_instrumentos_afinables(self):
        for instrumento in self.__instrumentos:
            if isinstance(instrumento, Afinable):
                instrumento.ejecutar()

if __name__ == "__main__":
    # f1 = Flauta()

    # f1.ejecutar()

    o = Orquesta()

    o.agregar(Flauta())
    o.agregar(Flauta())
    o.agregar(Guitarra())
    o.agregar(Arpa())

    print("Inicia la obra:")
    o.ejecutar_obra()

    # v = Viento()  # No se puede, porque Viento es clase abstracta

    print()
    print("Inicia la obra con instrumentos afinables:")
    o.ejecutar_obra_de_instrumentos_afinables()

    