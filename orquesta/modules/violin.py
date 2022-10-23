# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 19:13:54 2022

@author: DELL
"""
from modules.instrument import Instrument

class Violin(Instrument):
    
    
    def __init__(self):
        super().__init__("violin")
        print("Inicializador de Violin")
        
    def __del__(self):
        print("Destructor de Violin")
        
    def ejecutar_nota(self, nota):
        print("Violin ejecuta la nota: ", nota)


if __name__ == "__main__":
    
    
    v = Violin()
    
    print(v.get_nombre())