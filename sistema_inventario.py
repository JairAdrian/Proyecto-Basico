nombres = []
cantidades = []

while True:
    print("=" * 40)
    print(f"====Sistema de Inventario====")
    print(f"1. Agregar Producto")
    print(f"2. Ver Inventario")
    print(f"3. Buscar Producto")
    print(f"4. Actualizar cantidad")
    print(f"5. Eliminar producto")
    print(f"6. Total en stock")
    print(f"7. Salir")
    opc = int(input("Ingrese una opcion del menu:"))

    if opc == 1:
        nombre = input(f"Ingrese el nombre del producto:").lower()
        nombres.append(nombre)
        cantidad = int(input(f"Ingrese la cantidad del producto:"))
        cantidades.append(cantidad)
        print(f"Producto agregado correctamente.")
        print(f"=" * 40)
        print("\n")
    elif opc == 2:
        if not nombres:
            print("Esta vacia. no hay productos registrados.")
            continue
        
        print(f"====Lista de Productos====")
        for i, (nombre, cantidad ) in enumerate(zip(nombres, cantidades), 1):
            print(f"{i}. Producto: {nombre} - Cantidad: {cantidad}")
        print(f"=" * 40)
        print("\n")
    elif opc == 3:
        if not nombres:
            print("Esta vacia. no hay productos registrados.")
            continue
        buscar = input("Ingrese el nombre del producto a buscar:")
        encontrado = False

        for i, (nombre, cantidad ) in enumerate(zip(nombres, cantidades), 1):
            if nombre.lower() == buscar.lower():
                print(f"====Producto Encontrado====")
                print(f"Producto: {nombre} - Cantidada: {cantidad}")
                encontrado = True
                break
        else:
            print(f"Producto no encontrado")
        print(f"=" * 40)
        print("\n")
    elif opc == 4:
        if not nombres:
            print("Esta vacia. no hay productos registrados.")
            continue
        
        buscar1 = input("Ingrese el nombre del producto a actualizar:")
        encontrado1 = False

        for j, (nombre, cantidad ) in enumerate(zip(nombres, cantidades), 1):
            if nombre.lower() == buscar1.lower():
                print(f"====Producto Encontrado====")
                print(f"Producto: {nombre} - Cantidada: {cantidad}")
                nuevaCantidad = int(input("Ingrese la cantidad a actualizar:"))
                cantidades[j - 1] = nuevaCantidad
                print(f"Cantidad actualizada correctamente.")
                encontrado1 = True
                break
        else:
            print(f"Producto no encontrado.")
        print(f"=" * 40)
        print("\n")
        
    elif opc == 5:
        if not nombres:
            print("Esta vacia. no hay productos registrados.")
            continue
        
        buscar2 = input("Ingrese el nombre del producto a actualizar:")

        for n, ( nombre, cantidad ) in enumerate(zip(nombres, cantidades)):
            if nombre.lower() == buscar2.lower():
                print(f"===Producto Encontrado===")
                print(f"Producto: {nombre} - Cantidada: {cantidad}")
                nombres.pop(n)
                cantidades.pop(n)
                print("Producto eliminado correctamente.")
                break
        else:
            print("Producto no encontrado.")
        print(f"=" * 40)
        print("\n")
    elif opc == 6:
        if not nombres:
            print("Esta vacia. no hay productos registrados.")
            continue
        
        print("====Total de Stock en el inventario====")
        sumaStock = sum(cantidades)
        print(f"Total de productos: {sumaStock}")
        print(f"=" * 40)
        print("\n")

    elif opc == 7:
        print(f"Cerrando Menu.....")
        break
    else:
        print(f"Opcion invalida, coloque una opcion del menu")