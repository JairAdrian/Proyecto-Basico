
saldoActual = 100.0

while True:

    print("\n===Cajero Automatico===")
    print(f"\nMenu")
    print(f"1. Consutlar Saldo")
    print(f"2. Depositar")
    print(f"3. Retirar")
    print(f"4. Salir")
    opcion = int(input("Ingrese una opcion:"))

    if opcion == 1:
        print("=" * 40)
        print(f"Tu saldo actual es: S/{saldoActual}")
    elif opcion == 2:
        print("=" * 40)
        aumento = float (input("Ingrese el monto a depositar:"))
        print(f"Saldo anterior: S/{saldoActual}")
        saldoActual += aumento
        print(f"Saldo Actual: S/{saldoActual}")
    elif opcion == 3:
        print("=" * 40)
        print(f"Monto actual: S/{saldoActual}")
        retiro = float(input("Ingrese el monto a retirar:"))
        if retiro >= saldoActual:
            print(f"El retiro supera al saldo, retiro cancelado")
        else:
            print(f"El retiro exitoso.")
            saldoActual -= retiro
            print(f"Saldo Actual: S/{saldoActual}")
    elif opcion == 4:
        break