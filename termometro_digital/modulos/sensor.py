# -*- coding: utf-8 -*-

import random

class Sensor: 
    def __init__ (self):
        self._valor_minimo = 0.0
        self._valor_maximo = 5.0
        
    def sensar (self):
        valor_minimo = self._valor_minimo
        valor_maximo = self._valor_maximo
        valor = random.uniform(valor_minimo, valor_maximo)
        
        return valor