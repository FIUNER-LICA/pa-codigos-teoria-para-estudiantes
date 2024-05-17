# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:12:09 2023

@author: jorda
"""

from abc import ABC, abstractmethod


class Instrumento(ABC):
    @abstractmethod
    def ejecutar_nota(self):
        pass
    
    
class Afinable(Instrumento):
    @abstractmethod
    def afinar(self):
        pass


class Piano(Afinable):
    def ejecutar_nota(self):
        a = 3
        print("Ejecutar nota piano")

    def afinar(self):
        print("Se afina el piano")


class Violin(Afinable):
    def ejecutar_nota(self):
        c = 7
        v = 5*c
        print("Ejecutar nota violin")
        
    def afinar(self):
        g = 0
        print("Se afina el violin")


class Flauta(Instrumento):
    def ejecutar_nota(self):
        c = 7
        v = c**3
        print("Ejecutar nota flauta")
        

class Orquesta:
    def __init__(self):
        self.__instrumentos = []
    
    def agregar_instrumento(self, p_instrumento):
        self.__instrumentos.append(p_instrumento)
        
    def ejecutar_obra(self):
        for instrumento in self.__instrumentos:
            instrumento.ejecutar_nota()
            
    def afinar_instrumentos(self):
        for instrumento in self.__instrumentos:
            if isinstance(instrumento, Afinable):
                instrumento.afinar()


if __name__ == "__main__":
    # un_afinable = Afinable() # no tiene sentido
                             # es una clase abstracta
    
    # otra_flauta = Flauta()
    
    orquesta = Orquesta()  # clase concreta
    # orquesta.agregar_instrumento(otra_flauta)
    orquesta.agregar_instrumento(Piano())
    orquesta.agregar_instrumento(Violin())
    orquesta.agregar_instrumento(Flauta())
    
    # orquesta.agregar_instrumento("trompeta")  # Línea con un error: ¿Por qué?

    orquesta.afinar_instrumentos()
    print()
    orquesta.ejecutar_obra()
    
    # del orquesta  # se elimina objeto orquesta

    # otra_flauta.ejecutar_nota()    