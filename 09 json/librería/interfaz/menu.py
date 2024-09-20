def menu():
    while True:
        print("** LIBRERÍA **")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Salir")
        print("\n>> Opción?\n",end="")
        try:
            option=int(input())
            if option<1 or option>3:
                print("ERROR. Opción no válida.")
                input("Presione cualquier letra para volver al menu...")
                continue
            return option
        except ValueError:
            print("ERROR. Opción no válida.")
            input("Presione cualquier letra para volver al menu...")