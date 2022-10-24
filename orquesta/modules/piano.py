# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 19:13:35 2022

@author: DELL
"""
from modules.instrument import Instrument

class Piano(Instrument):
   
    def __init__(self):
        print("Inicializador de Piano")
        
    def __del__(self):
        print("Destructor de Piano")
    
    
    def ejecutar_nota(self, nota):
        print("Piano ejecuta la nota: ", nota)

