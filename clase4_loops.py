# EJERCICIO 1: Contador simple
# TODO: Usa un loop while para contar del 1 al 10
# TODO: Imprime cada número

# Escribe tu código aquí:
print(f"====Contador Simple====")
contador = 0
while contador <= 10:
    print(contador)
    contador += 1
print("=" * 40)

# EJERCICIO 2: Suma de números
# TODO: Usa un loop for con range(1, 101)
# TODO: Suma todos los números del 1 al 100
# TODO: Imprime el resultado total

# Escribe tu código aquí:
print("\n====Suma de 1 al 100====")
suma = 0
for i in range ( 1, 101 ):
    suma += i
print(f"La suma es: {suma}")
print("=" * 40)

# EJERCICIO 3: Tabla de multiplicar
# TODO: Pide al usuario un número
# TODO: Usa un loop for para mostrar su tabla de multiplicar (del 1 al 10)
# Ejemplo: Si ingresa 5, mostrar: 5x1=5, 5x2=10, ... 5x10=50

# Escribe tu código aquí:
print("\n====Tabla de Multiplicacion====")
numero = int(input("Ingrese un numero"))
for i in range(11):
    print(f"{numero} * {i} = {numero * i}"  )
print("=" * 40)

# EJERCICIO 4: Números pares
# TODO: Usa un loop for con range(1, 21)
# TODO: Imprime solo los números PARES
# PISTA: Usa continue para saltar los impares

# Escribe tu código aquí:
print("\n====Numeros Pares====")
for i in range(1, 21):
    if i % 2!= 0:
        continue
    print(i)
print("=" * 40)

# EJERCICIO 5: Buscar en lista
# TODO: Crea una lista: frutas = ["manzana", "banana", "naranja", "uva"]
# TODO: Pide al usuario el nombre de una fruta
# TODO: Usa un loop for para buscarla en la lista
# TODO: Si la encuentra, imprime "Fruta encontrada" y usa break
# TODO: Si no la encuentra (usa else), imprime "Fruta no disponible"

# Escribe tu código aquí:
print("\n====Buscar en listas====")
frutas = ["manzana", "banana", "naranja", "uva"]

buscar = input("Ingrese un nombre de fruta:").lower()

for fruta in frutas:
    if fruta == buscar:
        print(f"Fruta encontrada.")
        break
else:
    print(f"Fruta no encontrada.")
print("=" * 40)

# EJERCICIO 6: Contador de vocales
# TODO: Pide una frase al usuario
# TODO: Usa un loop for para recorrer cada letra
# TODO: Cuenta cuántas vocales (a,e,i,o,u) hay
# PISTA: usa lower() para convertir a minúsculas
# PISTA: verifica si la letra está en "aeiou"

# Escribe tu código aquí:
print("\n====Contador de Vocales====")
frase = input("Ingrese una frase:")
contadorVocales = 0
for letra in frase:
    if letra in "aeiou":
        contadorVocales += 1
print(f"La frase tiene {contadorVocales} vocales")
print("=" * 40)

# EJERCICIO 7: Validador de contraseña con intentos
# TODO: Define contraseña_correcta = "python123"
# TODO: Da al usuario 3 intentos para adivinar
# TODO: Usa un loop while o for con range(3)
# TODO: Si adivina, imprime "Acceso concedido" y break
# TODO: Si agota los 3 intentos, imprime "Cuenta bloqueada"

# Escribe tu código aquí:
contraseñaValida = "python123"
print(f"\n====Validar Contraseña====")

for intento in range(1, 4):
    contraseña = input(f"Intento {intento}/3 - Ingrese la contraseña:")
    if contraseña == contraseñaValida:
        print(f"Acceso concedido.")
        break
else:
    print(f"Acceso denegado.")
print("=" * 40)

# EJERCICIO 8: Menú con loop
# TODO: Crea un menú que se repita hasta que el usuario elija "Salir"
# Opciones:
# 1. Saludar
# 2. Despedirse  
# 3. Salir
# TODO: Usa while True y break

# Escribe tu código aquí:
while True:
    print(f"\n====Menu====")
    print(f"1. Saludar")
    print(f"2. Despedirse")
    print(f"3. Salir")
    opcion = int(input("Ingrese una opcion:"))

    if opcion == 1:
        print(f"Hola Usuario.")
    elif opcion == 2:
        print(f"Adios Usuario.")
    elif opcion == 3:
        print(f"Cerrando Menu....")
        break
    else:
        print(f"Opcion invalida, coloque un numero segun la opcion del menu.")
print("=" * 40)

# EJERCICIO 9: Pirámide de asteriscos
# TODO: Pide al usuario un número (altura de la pirámide)
# TODO: Usa loops anidados para crear una pirámide
# Ejemplo con altura 5:
# *
# **
# ***
# ****
# *****

# Escribe tu código aquí:
print(f"\n===Piramide de asteriscos===")
piramide = int(input(f"Ingrese la altura para la piramide:"))
for i in range (1, piramide + 1):
    print("*" * i)
print("=" * 40)

# EJERCICIO 10: Lista de compras
# TODO: Crea una lista vacía: compras = []
# TODO: Usa un loop while True
# TODO: Pide al usuario que ingrese productos
# TODO: Agrega cada producto a la lista con .append()
# TODO: Si escribe "fin", sal del loop con break
# TODO: Al final, muestra todos los productos con un for

# Escribe tu código aquí:

compras = []

while True:
    print(f"\n====Menu de Compras====")
    producto = input("Ingrese un producto ( o 'Fin' para terminar ):")
    if producto.lower() == "fin":
        break
    compras.append(producto)

print(f"\n===Tu Lista de Compras===")
for i, producto in enumerate(compras,1):
    print(f"{i}. {producto}")