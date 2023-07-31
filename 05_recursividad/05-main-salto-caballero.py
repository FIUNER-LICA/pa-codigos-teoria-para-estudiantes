# -*- coding: utf-8 -*-

def get_posiciones_validas(posicion: tuple[int, int], n: int) -> list[tuple[int, int]]:
    """
    Encuentra todas las posiciones válidas que el caballero puede realizar desde
    su posición actual.
    >>> get_posiciones_validas((1, 3), 4)
    [(2, 1), (0, 1), (3, 2)]
    """
    y, x = posicion
    posiciones = [
        (y + 1, x + 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 1, x - 2),
        (y + 2, x + 1),
        (y + 2, x - 1),
        (y - 2, x + 1),
        (y - 2, x - 1),
    ]
    posiciones_permitidas = []
    for pos in posiciones:
        y_test, x_test = pos
        if 0 <= y_test < n and 0 <= x_test < n:
            posiciones_permitidas.append(pos)
    return posiciones_permitidas


def tablero_completado(tablero: list[list[int]]) -> bool:
    """
    Verifica si el tablero se ha completado con valores diferentes de cero.
    """
    return not any(elem == 0 for fila in tablero for elem in fila)


def salto_del_caballo_auxiliar(
    tablero: list[list[int]], pos: tuple[int, int], actual: int) -> bool:
    """
    Función auxiliar para resolver el problema del salto del caballero.
    """
    if tablero_completado(tablero):
        return True

    for posicion in get_posiciones_validas(pos, len(tablero)):
        y, x = posicion

        if tablero[y][x] == 0:
            tablero[y][x] = actual + 1
            if salto_del_caballo_auxiliar(tablero, posicion, actual + 1):
                return True
            tablero[y][x] = 0

    return False


def recorrido_del_caballero(n: int) -> list[list[int]]:
    """
    Encuentra una solución para el problema del salto del caballero en un 
    tablero de tamaño n. Lanza un ValueError si el recorrido no puede ser 
    realizado debido al tamaño de tablero dado.
    """
    tablero = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            tablero[i][j] = 1
            if salto_del_caballo_auxiliar(tablero, (i, j), 1):
                return tablero
            tablero[i][j] = 0
    raise ValueError(f"La gira el caballero no puede ser realizada en un tablero de tamaño {n}x{n}")


if __name__ == "__main__":
    for fila in recorrido_del_caballero(5):
        print()
        for columna in fila:
            print(str(columna).zfill(2), end=' ')
    