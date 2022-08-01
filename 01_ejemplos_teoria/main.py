# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:06:41 2022

@author: entre todos
"""

# Ctrl + 1: para comentar!!!

# --------------------------
# como se hace un ciclo for
# --------------------------
# "Arreglo" (con una lista)
lista = [1, 2, 3, 4]

# Atenti: no se usa ";"
for valor in lista:
    print(valor)        # indentación para definir el "scope" del bucle

# iteramos utilizando "range"
print()
for i in range(len(lista)):
    print(lista[i])

# --------------------------
# como se hace una matriz
# --------------------------
# vamos a pensar una "lista de filas"
print()
matriz = [ [3, 4, 5], [6, 7, 8] ]
for f in range(2):
    print()
    for c in range(3):
        print(matriz[f][c], end=' ')

# --------------------------
# como se define una función
# --------------------------
print()
print()
def mi_funcion(pa, pb, pc):
    # pass
    r1 = (-pb + (pb**2 - 4*pa*pc)**(1/2))/(2*pa)
    r2 = (-pb - (pb**2 - 4*pa*pc)**(1/2))/(2*pa)
    return r1, r2

resultado1, resultado2 = mi_funcion(3, 4, 5)

print("resultado1 =", resultado1)
print("resultado2 =", resultado2)


## --------------------------
## como se hace un bucle while
## --------------------------
## Probaremos que el usuario ingrese un número positivo
## 1: pedirle al usuario que ingrese un número
## 2: iniciar un bucle para evaluar el número
## 2.1: comprobar si el valor es positivo --> condicional
#
#mensaje = ''  # se crea una cadena de caracteres vacía
#
#seguir = True
#
#while seguir:
#    numero = float(input("Por favor, ingrese un número: "))
#    #print(type(numero))
#
#    if numero > 0:
#        mensaje = 'El número es mayor que 0.'
#        seguir = False
#    else:
#        mensaje = 'El número NO es mayor que 0.'
#    print(mensaje)
#
#print('\n'*2)


# --------------------------
# como se hace un "if-elif-elif-else"
# --------------------------
# Determinar algunas categorías: joven (menor 25), adulto-joven (menor 50), adulto (menor 70) y anciano

#print('Por favor, ingrese su edad: ', end='')
#edad = int(input())
#
#if 0 <= edad <= 125:
#    if edad <= 25:
#        print('Eres joven.')
#    elif edad <= 50:
#        print('Eres adult@ joven')
#    elif edad <= 70:
#        print('Eres adult@')
#    else:
#        print('Eres ancian@')
#else:
#    print('Sos de otra dimensión...')
#

# --------------------------
# como se hace construye una dirección de correo electrónico
# a partir de un nombre y un apellido.
# --------------------------

nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")

#print(nombre[0])

#nombre[0] = 'T'  # no se puede porque los strings son inmutables

def crear_correo(pnombre, papellido):
    dominio = '@uner.edu.ar'
    inicial = pnombre[0]
    res_correo = inicial + papellido + dominio
    return res_correo.lower()

correo = crear_correo(nombre, apellido)
print(correo)



