# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 19:13:26 2022

@author: DELL
"""
from abc import ABC, abstractmethod

class Instrument(ABC):
    
   
    
    def __init__(self,nombre):
        print("Inicializador de Instrumento")
        self._nombre = nombre
    
    def get_nombre(self):
        return self._nombre
 
    def __del__(self):
        print("Destructor de Instrumento")
    
    @abstractmethod
    def ejecutar_nota(self, nota):
        pass
