from abc import ABC, abstractmethod

class Alimento(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._nombre = 'S/N'
    
    def get_nombre(self):
        return self.__nombre
    
    @abstractmethod
    def calcular_aw(self):
        pass

class Fruta(Alimento):
    pass

class Kiwi(Fruta):
    def __init__(self) -> None:
        super().__init__()
        self._nombre = 'Kiwi'
    
    def calcular_aw(self):
        return 0.8

class Cajon:
    def __init__(self) -> None:
        self.__alimentos = []

    def __iter__(self):
        return (alimento for alimento in self.__alimentos)

    def agregar_alimento(self, p_alimento):
        if isinstance(p_alimento, Alimento):
            self.__alimentos.append(p_alimento)
        else:
            raise TypeError('El objeto no es de la clase Alimento')
