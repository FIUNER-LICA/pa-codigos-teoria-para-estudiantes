# -*- coding: utf-8 -*-

import math
from abc import ABC, abstractmethod


class Figura(ABC):
    def __init__(self):
        self._nombre = None
        self.__area = None
        self.__perimetro = None
    
    def get_nombre(self):
        return self._nombre
    
    @abstractmethod
    def calcular_area(self):
        pass
        

class Cuadrado(Figura):
    def __init__(self, p_lado):
        super().__init__()
        self._nombre = "Cuadrado"
        self.__lado = p_lado
        
    def calcular_area(self):
        return self.__lado**2


class Circulo(Figura):
    def __init__(self, p_radio):
        super().__init__()
        self._nombre = "Circulo"
        self.__radio = p_radio

    def calcular_area(self):
        r = self.__radio
        pi = math.pi
        return round(pi*r**2, 3)
    
    
class Persona:
    def get_nombre(self):
        return "Carlos"
    
    def calcular_area(self):
        return 1.7
    

if __name__ == "__main__":
    # un_cuadrado = Cuadrado()
    # print(un_cuadrado.get_nombre())
    # print(un_cuadrado.__dict__)
    
    figuras = [Cuadrado(2),
               Circulo(1),
               Cuadrado(3),
               # Figura(), # No se puede crear una instancia de una clase abstracta.
               # Persona(), # Duck typing
               ]
    
    print()
    print("Figuras:")
    for figura in figuras:
        if isinstance(figura, Figura):
            print(figura.get_nombre())
            # print(figura._nombre) # funciona, pero no es correcto
            print('\t',
                  figura.calcular_area())
        else:
            raise TypeError("El objeto no es una Figura.")
