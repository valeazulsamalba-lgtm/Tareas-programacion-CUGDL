print("Este es el menú de la cafetería")
print("1. Café")
print("2. Capuchino")
print("3. Té")
print("4. Sándwich")

opcion = int(input("Selecciona una opción: "))

match opcion:
    case 1:
        print("Elegiste Café")
    case 2:
        print("Elegiste Capuchino")
    case 3:
        print("Elegiste Té")
    case 4:
        print("Elegiste Sándwich")
    case _:
        print("Opción no válida")
        