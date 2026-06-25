# Sistema de Gestión de Inventario

# Función de bienvenida
def mostrar_bienvenida(nombre):
    print("Bienvenido a control de inventarios", nombre)


# Entrada de datos
nombre_usuario = input("Ingresa tu nombre: ")

# Llamada a la función
mostrar_bienvenida(nombre_usuario)

# Lista de productos inicial
productos = ["Laptop", "Mouse", "Teclado"]

# Ciclo del menú
while True:

    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Ver estadísticas")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    # Match Case
    match opcion:

        case "1":
            print("\nLista de productos:")
            for i, producto in enumerate(productos, start=1):
                print(f"{i}. {producto}")

        case "2":
            nuevo_producto = input("Ingresa el nombre del nuevo producto: ")
            productos.append(nuevo_producto)
            print("Producto agregado correctamente.")

        case "3":
            eliminar_producto = input("Ingresa el nombre del producto a eliminar: ")
            if eliminar_producto in productos:
                productos.remove(eliminar_producto)
                print("Producto eliminado.")
            else:
                print("El producto no se encuentra en la lista.")

        case "4":
            total = len(productos)
            print("Total de productos en el inventario:", total)

        case "5":
            print("Saliendo del sistema...")
            break

        case _:
            print("Opción inválida. Intenta nuevamente.")