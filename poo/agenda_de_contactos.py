class Contacto:
    def __init__(self, p_nombre = "S/N", p_nro_tel = 0):
        self.__nombre = p_nombre
        self.__nro_telefono = p_nro_tel
        self.__correo_electronico = None

    def devolverNombre(self):
        return self.__nombre

    def establecerNroTelefono(self, p_nro_telefono):
        self.__nro_telefono = p_nro_telefono

    def devolverNroTelefono(self):
        return self.__nro_telefono

    def establecerCorreo(self, p_correo):
        if '@' in p_correo:
            self.__correo_electronico = p_correo
        else:
            raise Exception("Correo no tiene @.")
        
    def devolverCorreo(self):
        return self.__correo_electronico
    

class AgendaDeContactos:
    def __init__(self):
        print("se invoca inicializadr de AgendaDeContactos")
        self.__contactos = []
        self.__categoria = "Sin categorizar"
    
    def agregarContacto(self, p_contacto):
        print("se invoca agregarContacto")
        if not isinstance(p_contacto, Contacto):
            raise Exception("La variable no es de tipo Contacto.")
        if p_contacto not in self.__contactos:
            self.__contactos.append(p_contacto)


if __name__ == "__main__":
    contacto1 = Contacto("Ignacio", 284827482)
    contacto2 = Contacto("Ana", 12345678)

    if True:
        agenda1 = AgendaDeContactos()

        agenda1.agregarContacto(contacto1)
        agenda1.agregarContacto(contacto2)

        agenda2 = AgendaDeContactos()
        agenda2.agregarContacto(contacto1)

    
    


