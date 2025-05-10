# Ejemplo 10: Iteración en clase personalizada Poblacion

class Individuo:
    def __init__(self, codigo): 
        self.__codigo = codigo
    
    def __str__(self): 
        return "Individuo: " + self.__codigo   
    
class Poblacion:
    def __init__(self):
        self.__individuos = [Individuo('A'), Individuo('B'), Individuo('C')]
    
    def __iter__(self):
        self.__indice = 0
        return self # se retorna a sí mismo porque es un iterable
    
    def __next__(self):
        if self.__indice < len(self.__individuos):
            individuo = self.__individuos[self.__indice]
            self.__indice += 1
            return individuo
        else:
            raise StopIteration


# Ejemplo de uso
Poblacion = Poblacion() # Instancia de la clase Poblacion
for individuo in Poblacion: # Iteración sobre la población
    print(individuo)