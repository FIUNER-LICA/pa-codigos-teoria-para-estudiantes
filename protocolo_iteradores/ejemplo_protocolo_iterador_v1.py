class MiSecuencia:
    def  __init__(self) -> None:
        self.valores = [1,3,5,7]

    # def __iter__(self):
    #     return (x for x in self.valores)

    def __iter__(self):
        for x in self.valores:
            yield x

una_secuencia = MiSecuencia()

iterador = iter(una_secuencia)

print("una_secuencia:", una_secuencia)
print("iterador:", iterador)

for valor in una_secuencia:
    print(valor)