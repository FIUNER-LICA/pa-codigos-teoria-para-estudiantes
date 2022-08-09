# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 12:15:17 2022

@author: dz at fiuner
"""

# Ejemplo, modelar un Perro (mascota) que puede ladrar. La idea es crear una clase Perro, que tiene la propiedad nombre que es de lectura y escritura, la propiedad color que es de solo lectura y el método ladra.

class Perro:
    def __init__(self, p_nombre, p_color): 
        self._nom = p_nombre 
        self._col = p_color
    
    @property 
    def nombre(self): 
        return self._nom
    
    @nombre.setter 
    def nombre(self, p_nombre): 
        self._nom = p_nombre
    
    @property 
    def color (self): 
        return self._col
    
    def ladrar(self): 
        return "Guau!"

if __name__ == "__main__":
    # En este caso creamos un objeto de tipo perro con nombre johnny y color blanco. Luego otros dos con nombres morgan, rubia y angueto (fueron los nombres de algunas de las mascotas FIUNER, en otra época...)
    morgan = Perro('Morgan', 'negro')
    rubia = Perro('Rubian', 'marrón claro') 
    angueto = Perro('Angueto', 'marrón')
