nombres = []
cantidades = []

def mostrar_menu():
    print("====Sistema Inventario====")
    print("1. Registrar Producto")
    print("2. Ver inventario")
    print("3. Buscar producto")
    print("4. Actualizar Cantidad")
    print("5. Eliminar Producto")
    print("6. Calcular stock")
    print("7. Salir")
    print("=" * 40)

def agregar_producto():
    print("===Aregar un producto al inventario===")
    nombre = input("Ingrese el nombre del producto:")
    cantidad = int(input("Ingrese la cantidad del producto:"))

    nombres.append(nombre)
    cantidades.append(cantidad)

    print(f"Producto agregado correctamente.")
    print(f"{nombre} agregado con cantidad {cantidad}")
    print("=" * 40)
    print("\n")

def mostrar_inventario():
    if not nombres:
        print("Sin productos agregados")
        return
    
    print("====Lista de Productos====")
    for i, (nombre, cantidad) in enumerate(zip(nombres,cantidades)):
        print(f"{i}. Producto: {nombre} - Cantidad: {cantidad}")
    print("=" * 40)
    print("\n")

def buscar_producto():
    if not nombres:
        print("Sin productos agregados.")
        return
    
    buscar = input("Ingrese el nombre del producto a buscar:")
    encontrado = False

    for i, (nombre, cantidad) in enumerate(zip(nombres,cantidades)):
        if nombre.lower() == buscar.lower():
            print("===Producto Encontrado===")
            print(f"Producto: {nombre} - Cantidad: {cantidad}")
            encontrado = True
            break
    else:
        print("Producto no encontrado.")
    print("=" * 40)
    print("\n")

def actualizar_producto():
    if not nombres:
        print("Sin productos agregados.")
        return
    
    buscar = input("Ingrese el nombre del producto a actualizar:")
    encontrado = False

    for i, (nombre, cantidad) in enumerate(zip(nombres, cantidades)):
        if nombre.lower() == buscar.lower():
            print("===Producto encontrado===")
            print(f"Producto: {nombre} - Cantidad: {cantidad}")
            nuevoCantidad = int(input("Ingrese la nueva cantidad:"))
            cantidades[i] = nuevoCantidad
            print("===Cantidad actualizado correctamente===")
            encontrado = True
            break
    else:
        print("Producto no encontrado.")
    print("=" * 40)
    print("\n")

def eliminar_prodcuto():
    if not nombres:
        print("Sin productos registrados.")
        return
    buscar = input("Ingrese el nombre del producto a actualizar:")
    encontrado = False

    for i, (nombre, cantidad) in enumerate(zip(nombres, cantidades)):
        if nombre.lower() == buscar.lower():
            print("===Producto encontrado===")
            print(f"Producto: {nombre} - Cantidad: {cantidad}")
            nombres.pop(i)
            cantidades.pop(i)
            print("===Producto eliminado correctamente===")
            encontrado = True
            break

def calcular_total_stock():
    if not nombres:
        print("Sin productos registrados")
        return
    
    print("====Total de Stock en el inventario====")
    sumaStock = sum(cantidades)
    print(f"Total de productos: {sumaStock}")
    print(f"=" * 40)
    print("\n")

def main():
    while True:
        mostrar_menu()
        opc = int(input("Elige una opcion:"))

        if opc == 1:
            agregar_producto()
        elif opc == 2:
            mostrar_inventario()
        elif opc == 3:
            buscar_producto()
        elif opc == 4:
            actualizar_producto()
        elif opc == 5:
            eliminar_prodcuto()
        elif opc == 6:
            calcular_total_stock()
        elif opc == 7:
            print("Gracias por usar el sistema.")
            print("Cerrando el menu......")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()