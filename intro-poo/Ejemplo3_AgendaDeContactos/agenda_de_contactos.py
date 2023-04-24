# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:28:50 2023
@author: jfi
@author: dz
Este ejemplo se desarrolló en clases como un caso dicáctico para presentar composición y agregación.
"""

class Contacto:
    numero_de_contactos = 0
    
    def __init__(self, p_nom, p_correo):
        self.__nombre = p_nom
        self.__correo = p_correo
        Contacto.numero_de_contactos += 1
   

    @property
    def nombre(self):
        return self.__nombre


class AgrupacionDeContactos:
    """
    Modela un grupo que agrega contactos
    """
    def __init__(self):
        self.__contactos = {}
    
    def agregar_contacto(self, p_contacto):
        if isinstance(p_contacto, Contacto):
            nombre = p_contacto.nombre
            self.__contactos[nombre] = p_contacto
        else:
            raise Exception("El parámetro debe ser un Contacto")
    
    def quitar_contacto(self, p_nom):
        pass
    
    def __str__(self):
        """
        Muestra todos los contactos del grupo.
        """
        pass
    

class AgendaDeContactos:
    """
    Modela una agenda que tiene contactos
    """
    def __init__(self):
        self.contactos = {}
        
    def agregar_contacto(self, p_nom, p_correo):
        un_contacto = Contacto(p_nom, p_correo)
        if p_nom not in self.contactos:
            self.contactos[p_nom] = un_contacto
        else:
            raise Exception("El nombre ya existe")
    
    def eliminar_contacto(self, p_nom):
        del self.contactos[p_nom]
    
    def devolver_contacto(self, p_nom):
        return self.contactos[p_nom]
    

if __name__ == "__main__":
    agenda_de_contactos = AgendaDeContactos()
    agenda_de_contactos.agregar_contacto("Juan", "juan@email.com")
    agenda_de_contactos.agregar_contacto("Aixa", "aixa@email.com")
    agenda_de_contactos.agregar_contacto("Manuel", "manuel@email.com")
    agenda_de_contactos.agregar_contacto("Carla", "carla@email.com")
    
    una_agrupacion = AgrupacionDeContactos()
    
    el_contacto = agenda_de_contactos.devolver_contacto("Manuel")
    print("el_contacto.numero_de_contactos:", 
          el_contacto.numero_de_contactos)
    
    una_agrupacion.agregar_contacto(el_contacto)
    el_contacto = agenda_de_contactos.devolver_contacto("Carla")
    una_agrupacion.agregar_contacto(el_contacto)

    print("el_contacto.numero_de_contactos:", 
           el_contacto.numero_de_contactos)