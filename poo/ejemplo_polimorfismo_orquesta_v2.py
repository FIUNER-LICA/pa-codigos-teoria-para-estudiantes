# -*- coding: utf-8 -*-


class Guitarra:
    def ejecutar(self):
        print("ejecutar nota guitarra")

class Arpa:
    def ejecutar(self):
        print("ejecutar nota arpa")

class Flauta:
    def ejecutar(self):
        c = 4
        # código específico para ejecutar una flauta
        print("ejecutar nota flauta")


class Orquesta:
    def __init__(self) -> None:
        self.__instrumentos = []
    
    def agregar(self, p_instrumento):
        no_pertenece_aun = p_instrumento not in self.__instrumentos
        if no_pertenece_aun:
            self.__instrumentos.append(p_instrumento)
        else:
            raise Exception("O no es subclase, o ya pertenece a la orquesta.")

    def ejecutar_obra(self):
        for instrumento in self.__instrumentos:
            instrumento.ejecutar()

    def ejecutar_obra_de_instrumentos_afinables(self):
        for instrumento in self.__instrumentos:
            if isinstance(instrumento, Guitarra) or isinstance(instrumento, Arpa):
                instrumento.ejecutar()


class MartilloNeumatico:
    def ejecutar(self):
        print("ejecutar máquina")


if __name__ == "__main__":
    # f1 = Flauta()

    # f1.ejecutar()

    o = Orquesta()

    o.agregar(Flauta())
    o.agregar(Flauta())
    o.agregar(Guitarra())
    o.agregar(Arpa())

    # o.agregar(MartilloNeumatico()) # ¡¿What?!

    print("Inicia la obra:")
    o.ejecutar_obra()

    # v = Viento()  # No se puede, porque Viento es clase abstracta

    print()
    print("Inicia la obra con instrumentos afinables:")
    o.ejecutar_obra_de_instrumentos_afinables()

    