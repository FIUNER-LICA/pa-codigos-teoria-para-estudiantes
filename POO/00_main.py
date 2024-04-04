lista_1 = [1, 2, 3]
lista_2 = [1, 2, 3]

print("Estado lista_1:", lista_1)
print("Estado lista_2:", lista_2)

print("Dirección de memmoria lista_1:",
      hex(id(lista_1)))
print("Dirección de memmoria lista_2:",
      hex(id(lista_2)))

a = 1
b = 1
print()
print("Estado a:", a)
print("Estado b:", b)
print("Dirección de 'a' en la memoria:",
      hex(id(a)))
print("Dirección de 'b' en la memoria:",
      hex(id(b)))

b = 2
print()
print("Estado a:", a)
print("Estado b:", b)
print("Dirección de 'a' en la memoria:",
      hex(id(a)))
print("Dirección de 'b' en la memoria:",
      hex(id(b)))

# ejemplo excepción en lista
print(lista_1[1000])

print("Este texto no se verá...")