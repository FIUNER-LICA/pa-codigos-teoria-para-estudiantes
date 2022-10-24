# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 10:20:15 2022

@author: dz
Ejemplo de arquitectura de una aplicación de simulación.

Se ha tomado el ejemplo rain del libro de Rouggier, el cual presenta una animación de una lluvia. A partir de este ejemplo, se trabajó en la separación de dependencias del ejemplo mediante la creación de una clase Animador, una clase Modelo y una clase Controlador de la simulación.
"""

from controlador import ControladorDeSimulador


cs = ControladorDeSimulador()

opcion = 1
while opcion != 99:
    print("1. Simular y graficar ")
    print("2. Pausar")
    print("3. Continuar simulando")
    print("99. para salir")
    opcion = int (input("Opción: "))
    if opcion == 1:
        cs.simular_y_graficar()      
    elif opcion == 2:
        cs.pausar_simulacion()
        continue
    elif opcion == 3:
        cs.continuar_simulacion()
        continue
    elif opcion != 99:
        print ("opcion inválida")
        
        