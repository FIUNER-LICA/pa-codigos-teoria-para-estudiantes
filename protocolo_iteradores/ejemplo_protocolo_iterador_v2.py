class IteradorCuboDeXHasta10DeA2:
    def __init__(self, p_x) -> None:
        self.__x = p_x

    def __next__(self):
        if self.__x < 10:
            resultado = self.__x**3
            self.__x += 2
            return resultado
        else:
            raise StopIteration

class MiSecuencia2:
    def  __init__(self) -> None:
        self.valor_de_x_inicial = 3

    def __iter__(self):
        return IteradorCuboDeXHasta10DeA2(self.valor_de_x_inicial)


una_secuencia = MiSecuencia2()

iterador = iter(una_secuencia)

print("una_secuencia:", una_secuencia)
print("iterador:", iterador)

for valor in una_secuencia:
    print(valor)