from POO.desacople.modulos.factoria import crear_repositorio
from modulos.entidades import Libro

repositorio = crear_repositorio()

def main():
    while True:
        print('-*-'*30) # separador

        # Desplegar menú
        print("Opciones:")
        print("\t1 - Listar libros.")
        print("\t2 - Crear un libro.")
        print("\t3 - Editar un libro.")
        print("\t4 - Borrar un libro.")
        print("\t5 - Salir.")
        
        # Capturar opción válida
        opcion = None
        try:
            opcion = int(input("Seleccionar una opción (ingrese un número entero): "))
        except ValueError:
            break # Sale del bucle que controla menú principal

        # Procesar opciones
        if opcion == 1:
            print("Opcion elegida: Listar libros.")

            lista_de_libros = repositorio.get_lista_libros()   
            
            for libro in lista_de_libros:
                print(f'\tId {libro.get_id()})', libro)

        elif opcion == 2:
            print("Opcion elegida: Crear un libro.")
            
            # Se ingesan datos
            nombre = input("\tIngrese el nombre del libro:")
            autor = input("\tIngrese el autor del libro:")
            while True:
                try:
                    puntaje = float(input("\tIngrese el puntaje del libro (0.0 a 10.0):"))
                except ValueError as err:
                    print("Error: ingese un puntaje válido (número real de 0.0 a 10.0).")
                else:
                    break
            
            # Se guarda libro
            try:
                libro = Libro(None, nombre, autor, puntaje)
                repositorio.guardar_libro(libro)
            except (ValueError, TypeError) as err:
                print("Error:", err)

        elif opcion == 3:
            print("Opcion elegida: Editar un libro.")
            
            while True:
                try:
                    id_libro = int(input("Ingrese el id del libro (ver lista de libros):"))
                    if id_libro < 1:
                        raise ValueError
                except ValueError as err:
                    print("Error: ingese un id válido (número entero positivo).")
                else:
                    break
            
            try:
                libro = repositorio.leer_libro(id_libro)
            except ValueError as err:
                print("Error:", err)
            else:
                print("Datos del libro seleccionado:")
                print("\tNombre:", libro.get_nombre())
                print("\tAutor:", libro.get_autor())
                print("\tPuntaje:", libro.get_puntaje())
                print()
                
                print("Ingrese los datos actualizados para este libro:")
                
                nombre = input("Nombre (deje vacío para no modificar):")
                autor = input("Autor (deje vacío para no modificar):")
                puntaje = input("Puntaje (número real, deje vacío para no modificar):")
                
                if len(nombre) > 0:
                    libro.set_nombre(nombre)
                if len(autor) > 0:
                    libro.set_autor(autor)
                if len(puntaje) > 0:
                    libro.set_puntaje(float(puntaje))

                repositorio.actualizar_libro(libro)

        elif opcion == 4:
            print("Opcion elegida: Borrar un libro.")

            while True:
                try:
                    id_libro = int(input("Ingrese el id del libro (ver lista de libros):"))
                    if id_libro < 1:
                        raise ValueError
                except ValueError as err:
                    print("Error: ingese un id válido (número entero positivo).")
                else:
                    break
            
            try:
                libro = repositorio.leer_libro(id_libro)
            except ValueError as err:
                print("Error:", err)
            else:
                print("Datos del libro seleccionado:")
                print("\tNombre:", libro.get_nombre())
                print("\tAutor:", libro.get_autor())
                print("\tPuntaje:", libro.get_puntaje())
                print()

                confirmacion = input('¿Está seguro de que desea eliminarlo? (responda SI para eliminar):')

                if confirmacion == 'SI':
                    repositorio.borrar_libro(libro)
                else:
                    print("Operación de borrado cancelada.")
        else:
            break
        print('-*-'*30) # separador
    
    print("\n¡Nos vemos pronto!\n")
    
main()