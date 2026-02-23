
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
        aumento = float(input("Ingrese el monto a depositar: "))
        if aumento <= 0:
            print("❌ Error: El monto debe ser mayor a 0")
        else:
            print(f"Saldo anterior: S/{saldoActual:.2f}")
            saldoActual += aumento
            print(f"✅ Depósito exitoso")
            print(f"Saldo actual: S/{saldoActual:.2f}")
    elif opcion == 3:
        print("=" * 40)
        print(f"Monto actual: S/{saldoActual:.2f}")
        retiro = float(input("Ingrese el monto a retirar:"))
        if retiro < 10:
            print("❌ El retiro mínimo es S/10")
        elif retiro > 500:
            print("❌ El retiro máximo por operación es S/500")
        elif retiro > saldoActual:  # Tu validación estaba casi bien
            print("❌ Saldo insuficiente. Retiro cancelado")
        else:
            saldoActual -= retiro
            print("✅ Retiro exitoso")
            print(f"Saldo actual: S/{saldoActual:.2f}")
    elif opcion == 4:
        break
    else:
        print("❌ Opción inválida. Por favor elige 1-4")
