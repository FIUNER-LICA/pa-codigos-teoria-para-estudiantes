# while True:
#     try:
#         x = int(input("Por favor, ingrese un número entero:"))
#         break
#     # except (ValueError, NameError):
#     #     print("Ups, el valor ingresado no es válido")
#     except ValueError:
#         print("Ups, el valor ingresado no es válido")
#     except NameError:
#         print("Ups, error de nombre")

# try:
#     x = int(input("Por favor, ingrese un número entero:"))
# except ValueError:
#     print("Ups, el valor ingresado no es válido")
# print("El valor ingresado es:", x)  # ¡Ojo, que esto puede gerar otra excepción si x no existe!

# try:
#     x = int(input("Por favor, ingrese un número entero:"))
# except ValueError:
#     print("Ups, el valor ingresado no es válido")
# else:
#     print("El valor ingresado es:", x)

class ValorNegativo(Exception):
    pass

try:
    x = int(input("Por favor, ingrese un número entero:"))
    if x<0:
        raise ValorNegativo("El valor no puede ser negativo, porque representa una cantidad.")
except ValueError:
    print("Ups, el valor ingresado no es válido")
except ValorNegativo as mi_err:
    print("Ups, el valor ingresado no puede ser negativo")
    print("El mensaje de error es:", mi_err)
else:
    print("El valor ingresado es:", x)
