class EntidadGeometrica:
    def __init__(self):
        self._area = 0  # atributo protegido!
        
    def get_area(self):
        return self._area


class Cuadrado(EntidadGeometrica):
    def __init__(self, p_lado):
        super().__init__()
        self.__lado = p_lado
        self._area = self.__lado**2
        

class Cubo(EntidadGeometrica):
    def __init__(self, p_longitud_arista):
        super().__init__()
        self.__longitud_arista = p_longitud_arista
        self._area = self.__longitud_arista**2*6


if __name__ == "__main__":
    cuadrado = Cuadrado(4)
    print("Área cuadrado:", cuadrado.get_area())

    cubo = Cubo(3)
    print("Área cubo:", cubo.get_area())