import math
import random

def trapz(li, ls, h, funcion):
    I = funcion(li) + funcion(ls)
    i = li + h
    while i < ls:
        I += 2 * funcion(i)
        i += h
    return I * h / 2

def simpson(li, ls, h, funcion):
    I = funcion(li) + funcion(ls)
    N = int((ls - li) / h)
    for j in range(1, N - 2, 2):
        I += 4 * funcion(li + j * h)
    for i in range(2, N - 1, 2):
        I += 2 * funcion(li + i * h)
    return I * h / 3

def mc_c(li, ls, N, funcion):
    I = 0.0
    for _ in range(N):
        r = li + random.uniform(0, 1) * (ls - li)
        I += funcion(r)
    return (ls - li) / N * I

def main():
    Li = 0.0
    Ls = math.pi
    h = 0.01
    funcion = math.sin
    print("-----------------------------------------------------------")
    print("Comparación de la integral de la función seno [0, pi]")
    print("utilizando cuatro métodos distintos.")
    print("------------------------------------------------------------")
    print("Limite inf.: ", Li)
    print("Limite sup.: ", Ls)

    I_trap = trapz(Li, Ls, h, funcion)
    I_simpson = simpson(Li, Ls, h, funcion)
    N = int((Ls - Li) / h)
    I_mc = mc_c(Li, Ls, N, funcion)

    print("{:<12} {:<12} {:<12} {:<12} {:<12}".format('Método', 'Resultado', 'Error Abs', 'Error Rel', 'Cota Error'))
    print("{:<12} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format('Trapecio', I_trap, 2.0 - I_trap, abs(2.0 - I_trap) / 2.0 * 100, pow(h, 3) / 12))
    print("{:<12} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format('Simpson', I_simpson, 2.0 - I_simpson, abs(2.0 - I_simpson) / 2.0 * 100, pow(h, 4) / 180))
    print("{:<12} {:<12.6f} {:<12.6f} {:<12.6f}".format('Montecarlo', I_mc, 2.0 - I_mc, abs(2.0 - I_mc) / 2.0 * 100))

if __name__ == "__main__":
    main()