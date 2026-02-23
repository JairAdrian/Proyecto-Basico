while True:
    nombre = input("Ingrese el nombre del alumno:")
    nota1 = int(input("Ingrese la primera nota:"))
    nota2 = int(input("Ingrese la segunda nota:"))
    nota3 = int(input("Ingrese la tercera nota:"))
    nota4 = int(input("Ingrese la cuarta nota:"))
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    print("=" * 40)
    print(f"Promedio final: {promedio}")

    if( promedio >= 13 ):
        print(f"Estado: Aprobado")
        print(f"¡Fecilitaciones!")
        print("=" * 40)
    else:
        print(f"Estado: Desaprobado:")
        print(f"Toca estudiar más.")
        print("=" * 40)

    continuar = input("Desea ingresar otro dato? ( S / N):")
    if( continuar == "N"):
        print("Gracias por usar el sistema.")
        break
