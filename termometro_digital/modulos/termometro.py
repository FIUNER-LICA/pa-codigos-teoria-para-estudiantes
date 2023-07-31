# -*- coding: utf-8 -*-

from modulos.sensor import Sensor 
from modulos.conversor import Conversor

class Termometro: 
    def __init__ (self): 
        self.sensor = Sensor()
        self.conversor = Conversor()
    
    def medir_temperatura(self):
        
        volt = self.sensor.sensar()
        temp = self.conversor.convertir(volt)
        
        return round (temp,2)