class Estudiante:
    '''
    Modela un@ estudiante universitari@.
    '''
    cantidad_estudiantes = 0

    def __init__(self, p_nombre = "S/N"):
        self.__nombre = p_nombre        
        self.__carrera = ""
        Estudiante.cantidad_estudiantes += 1

    def devolverNombre(self):
        return self.__nombre
    
    # def get_carrera(self):
    #     return self.__carrera

    # def set_carrera(self, p_carrera):
    #     self.__carrera = p_carrera

    @property
    def carrera(self):      # esto va a ser el getter
        print("se invoca al getter")
        return self.__carrera

    @carrera.setter
    def carrera(self, p_carrera):
        print("se invoca al setter")
        if p_carrera != "":
            self.__carrera = p_carrera
        else:
            raise Exception("La carrera no puede estar vacía")
    
    def __str__(self):
        cad = ""
        cad += self.__nombre
        cad += ", " + self.carrera
        return cad

print("cantidad_estudiantes:", Estudiante.cantidad_estudiantes)

un_estudiante = Estudiante("Pedro")
otro_estudiante = Estudiante()

print("cantidad_estudiantes:", Estudiante.cantidad_estudiantes)
print("cantidad_estudiantes:", un_estudiante.cantidad_estudiantes)

# un_estudiante.set_carrera("Lic. en Bioinformática")
# otro_estudiante.set_carrera("TUPED")

print(un_estudiante.devolverNombre())
print(otro_estudiante.devolverNombre())

un_estudiante.carrera = "Lic. en Bioinformática"
print(un_estudiante.carrera)

# otro_estudiante.carrera = ""  # Se lanza excepción por estar la cadena vacía

print()
print(un_estudiante)

