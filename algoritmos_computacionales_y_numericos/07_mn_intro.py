def machine_epsilon():
    """	Retorna el epsilon de la máquina. """
    epsilon = 1.0
    while (1.0 + 0.5 * epsilon) != 1.0:
        epsilon *= 0.5
    return epsilon

print("El épsilon de la máquina es:", machine_epsilon())


def division_test():
    a = 1.0
    b = 3.0
    result = a / b
    expected_result = 0.33333333333333333
    error = abs(result - expected_result)
    print("Resultado de la división: ", result)
    print("Resultado esperado: ", expected_result)
    print("Error absoluto: ", error)

division_test()

""" El siguiente código imprime la representación en punto flotante de 0.1 
con 55 dígitos de precisión. La representación en punto flotante de 0.1 no es exactamente 0.1,
lo que demuestra la limitación de la precisión en punto flotante."""	
a = 0.1
print("Representación en punto flotante de 0.1: ", "{0:.55f}".format(a))
