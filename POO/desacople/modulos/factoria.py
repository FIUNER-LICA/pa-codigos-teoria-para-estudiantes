from modulos.repositorio_concreto import RepositorioSQL


def crear_repositorio():
    return RepositorioSQL()
    #return RepositorioCSV()
