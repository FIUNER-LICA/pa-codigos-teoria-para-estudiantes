# -*- coding: utf-8 -*-

from modulos.termometro import Termometro 
import time


termometro = Termometro()

seguir = True

while True:
    time.sleep(1)
    temperatura = termometro.medir_temperatura()
    print("La temperatura es: ", temperatura)

