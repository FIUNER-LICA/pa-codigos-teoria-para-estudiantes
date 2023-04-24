class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.siguiente = None

class ListaReproduccion:
    def __init__(self):
        self.primer_cancion = None
        
    def agregar_cancion(self, titulo, artista, duracion):
        nueva_cancion = Cancion(titulo, artista, duracion)
        if self.primer_cancion is None:
            self.primer_cancion = nueva_cancion
        else:
            ultima_cancion = self.primer_cancion
            while ultima_cancion.siguiente is not None:
                ultima_cancion = ultima_cancion.siguiente
            ultima_cancion.siguiente = nueva_cancion
    
    def __iter__(self):
        current = self.primer_cancion
        while current is not None:
            yield current
            current = current.siguiente

if __name__ == "__main__":
    lista = ListaReproduccion()
    lista.agregar_cancion("Bohemian Rhapsody", "Queen", 354)
    lista.agregar_cancion("Hotel California", "Eagles", 390)
    lista.agregar_cancion("Stairway to Heaven", "Led Zeppelin", 482)

    iterator = iter(lista)
    print(type(iterator))

    for cancion in lista:
        print(cancion.titulo, cancion.artista, cancion.duracion)