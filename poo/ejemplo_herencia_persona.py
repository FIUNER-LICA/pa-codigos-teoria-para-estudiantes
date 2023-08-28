class Persona:
    def __init__(self, p_nombre, p_dni) -> None:
        self.__nombre = p_nombre
        self.__dni = p_dni
        self.__nro_telefono = None
        self.__correo_electronico = None
        print("se invoca __init__ de Persona")
        self._atributo_protegido = 35
        self.atributu_publico = 10

    def get_nombre(self):
        return self.__nombre

    def registrarTarjetaSUBE(self):
        print("se invoca registrarTarjetaSUBE de Persona")

    def descontarTarjetaSUBE(self):
        print("se invoca descontarTarjetaSUBE de Persona")


class Estudiante(Persona):
    def __init__(self, p_nombre, p_dni) -> None:
        super().__init__(p_nombre, p_dni)
        self.__nivel_estudios = "secundario completo"
        print("se invoca __init__ de Estudiante")

    def descontarTarjetaSUBE(self):
        print("se invoca descontarTarjetaSUBE de Estudiante")

    def acceder_a_atributo_protegido(self):
        print("Valor del atributo protegido:", self._atributo_protegido)


class Trabajador(Persona):
    def __init__(self, p_nombre, p_dni) -> None:
        super().__init__(p_nombre, p_dni)
        self.__sueldo = 20000
        print("se invoca __init__ de Trabajador")

    # def descontarTarjetaSUBE(self):
    #     print("se invoca descontarTarjetaSUBE de Trabajador")


if __name__ == "__main__":
    e1 = Estudiante("Carlos", 1234)
    e1.acceder_a_atributo_protegido()
    # print(e1._atributo_protegido)  # no se recomienda acceder desde le ámbito público a un atributo "protegido" por convención
    print(e1.atributu_publico)
    print("e1.get_nombre():", e1.get_nombre())
    e1.descontarTarjetaSUBE()


    t1 = Trabajador("Elena", 4321)
    print("t1.get_nombre():", t1.get_nombre())
    t1.descontarTarjetaSUBE()