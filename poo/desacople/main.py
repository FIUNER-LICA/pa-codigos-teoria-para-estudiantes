from modulos.configuraciones import crear_repositorio

repositorio = crear_repositorio()

def main():
    while True:
        # Desplegar menú
        print("Opciones:")
        print("\t1 - Listar libros.")
        print("\t2 - Ver un libro.")
        print("\t3 - Editar un libro.")
        print("\t4 - Borrar un libro.")
        print("\t5 - Salir.")
        
        opcion = int(input("Seleccionar una opción (ingrese un número entero): "))
        
        if opcion == 1:
            print("Opcion elegida: Listar libros.")
            
        elif opcion == 2:
            print("Opcion elegida: Ver un libro.")
        elif opcion == 3:
            print("Opcion elegida: Editar un libro.")
        elif opcion == 4:
            print("Opcion elegida: Borrar un libro.")
        else:
            break
    
    print("\n¡Nos vemos pronto!\n")
    
main()