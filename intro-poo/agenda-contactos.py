# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 12:15:17 2022

@author: dz at fiuner
"""
# Ejemplo de clase que modela una agenda de contactos
# Actualmente la mayoría de los dispositivos que utilizam nuestra vida cotidiana (teléfonos móviles, etc.) contienen agenda de contactos que nos permite mantener nuestros contactos organizados y encontrarlos rápidamente. En este ejemplo crearemos una clase AgendaContactos que modelará el funcionamiento esperado de este objeto.

# Esta agenda funcionará haciendo uso de un diccionario.

# 1. La agenda es básicamente una estructura de datos contenedora que maneja y organiza información.
# 2. Crearemos una clase en Python para que modela funcionamiento de una agenda que almacena el nombre contacto, su teléfono, y dirección de email.
# 3. Comenzamos definiendo la clase AgendaContactos y su inicializador
# 4. Seguidamente implementamos las operaciones de agragar, borrar y actualizar (proceso también conocido como ABM, de Alta, Baja y Modificación).
# 5. Para conocer las entradas de la agenda se tendrá el método imprimir para mostrar por consola las entradas de la agenda.

class AgendaContactos:
    
    def __init__(self):
        self.dicc = {}
    
    def agregar(self,p_nombre, p_num_tel,p_email):
        self.dicc[p_nombre] = (p_num_tel,p_email)
    
    def borrar(self,p_nombre):
        del self.dicc[p_nombre]
        
    def actualizar(self,p_nombre, p_datos):
        self.dicc[p_nombre] =  p_datos
        
        
    def imprimir(self):
        for nombre in self.dicc:
            print(nombre,self.dicc[nombre])
    
    @property 
    def cantidad(self): 
        return len(self.dicc)
    


if __name__ == "__main__":
    
    # implementación básica de pruebas de la clase agenda
    
    # Se crea una agenda
    print('Se crea una agenda')
    miAgenda = AgendaContactos()
    # se agregan 4 contactos
    print('se agregan 4 contactos')
    miAgenda.agregar('Kurt Gödel', 5354131966, 'kgodel@mail.com')
    miAgenda.agregar('Donald Knuth', 5354131954, 'dknuth@mail.com') 
    miAgenda.agregar('Alan Turing', 5353317102, 'aturing@mail.com')
    miAgenda.agregar('Ada Lovelace', 5353317139, 'alovelace@otro_mail.com')
    
    # Se imprime en pantalla la agenda
    print('Se imprime en pantalla la agenda')
    miAgenda.imprimir()

    # se actualiza un contacto
    print('se actualiza un contacto')
    miAgenda.actualizar('Donald Knuth', (5354131954,'dknuth@themail.com'))

    print('Se imprime en pantalla la agenda')
    miAgenda.imprimir()
    # Se borra un contacto
    print('Se borra contacto Alan Turing')
    miAgenda.borrar('Alan Turing')
    miAgenda.imprimir()

