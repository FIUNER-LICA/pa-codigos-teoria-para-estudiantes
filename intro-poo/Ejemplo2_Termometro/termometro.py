# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:04:00 2023

@author: DELL
"""

import random






class Sensor:
    """
    Modela un sensor capaz de medir la temperatura ambiente. 
    """
    def sensar(self):
        return random.random()*5.0 


class Conversor:
    """
    Convierte unidades de voltaje
    a temperatura en Celcius
    """
    def convertir(self, p_voltaje):
        resultado = 0.0
        resultado = -10 + p_voltaje*(100-(-10))/(5.0-0.0)
        return resultado
        

class Termometro:
    def __init__(self):
        self.__sensor = Sensor()
        self.__conversor = Conversor()
    
    def medir(self):
        temperatura = 0.0
        voltaje = self.__sensor.sensar() 
        temperatura = self.__conversor.convertir(voltaje)
        return temperatura


if __name__ == "__main__":
    # aquí colocamos pruebas 
    # sencillas
    termometro_de_prueba = Termometro()
    
    for _ in range(20):
        una_medicion = termometro_de_prueba.medir()
        print("una_medicion:", una_medicion)

    un_conversor = Conversor()
    
    print("Convertir 0.0 voltios:", un_conversor.convertir(0.0))
    print("Convertir 5.0 voltios:", un_conversor.convertir(5.0))


