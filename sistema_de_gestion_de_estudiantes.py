
def menu():
    print("=" * 40)
    print("====Gestion de estudiantes====")
    print("1. Agregar Estudiante")
    print("2. Mostrar Estudiantes")
    print("3. Calcular promedio de un estudiante")
    print("4. Salir")

def agregar_estudiante(estudiantes):
    print("=" * 40)
    nombre = pedir_nombre(estudiantes)
    edad = pedir_numero("Ingrese la edad del estudiante:", int, minimo=0, maximo=120)
    notas = []
    cantidad = pedir_numero("Ingrese la cantidad de notas:", int, minimo=1)
    
    for i in range(cantidad):
        nota = pedir_numero(f"Ingrese la nota{i+1}: ", float, minimo = 0, maximo = 20)
        notas.append(nota)

    estudiantes[nombre] = {
        "Edad" : edad,
        "Notas" : notas
    }

def pedir_nombre(estudiantes):
    while True:
        nombre = input("Ingrese el nombre del estudiante:")

        if not nombre:
            print("El nombre no puede estar vacio.")
            continue

        if nombre in estudiantes:
            print("El nombre ya esta registrado.")
            continue

        return nombre

def pedir_numero(mensaje, tipo=float, minimo=None, maximo=None):
    while True:
        try:
            numero = tipo(input(mensaje))

            if minimo is not None and numero < minimo:
                print(f"El numero debe ser mayor o igual a {minimo}")
                continue

            if maximo is not None and numero > maximo:
                print(f"El numero debe ser menor o igual a {maximo}")
                continue
            
            return numero
                
        except ValueError:
            print("Numero invalida. Intente nuevamente")

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("Sin estudiantes registrados.")
        return
    listar_estudiantes(estudiantes)
    print("=" * 40)
    print("\n")

def listar_estudiantes(estudiantes):
    
    print("====Lista de Estudiantes====")
    for nombre, datos in estudiantes.items():
        print(f"Nombre: {nombre}")
        print(f"Edad: {datos['Edad']}")
        print(f"Notas: {datos['Notas']}")

def calcular_promedio(estudiantes):
    
    buscar = input("Ingrese el nombre del estudiante")

    promedio = obtener_promedio(estudiantes, buscar)

    if promedio is None:
        print("Estudiante no encontrado.")
    elif promedio == 0:
        print("No hay notas ingresados.")
    else:
        print(f"El promedio de {buscar} es: {promedio:.2f}")

    print("=" * 40)
    print("\n")

def obtener_promedio(estudiantes, nombre):
    if nombre not in estudiantes:
        return None
    
    notas = estudiantes[nombre]["Notas"]

    if not notas:
        return 0
    
    return sum(notas) / len(notas)

# Programa principal
def main():
    estudiantes = {}

    while True:
        menu()
        opc = input("Ingrese una opcion:")

        if opc == "1":
            agregar_estudiante(estudiantes)
        elif opc == "2":
            mostrar_estudiantes(estudiantes)
        elif opc == "3":
            calcular_promedio(estudiantes)
        elif opc == "4":
            print("Cerrando Programa.....")
            break
        else:
            print("Opcion invalida.")
            print("=" * 40)
            print("\n")