# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 19:14:09 2022

@author: DELL
"""
from modules.instrumet import Instrument

class Violin(Instrument):
    
    def __init__(self):
        print("Inicializador de Flauta")
        

    def ejecutar_nota(self, nota):
        print("Flauta ejecuta la nota: ", nota)
