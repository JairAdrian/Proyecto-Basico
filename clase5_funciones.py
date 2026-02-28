# EJERCICIO 1: Función simple
# TODO: Crea una función llamada 'mostrar_bienvenida' que imprima "Bienvenido al programa"
# TODO: Llámala 3 veces

# Escribe tu código aquí:

def mostrarBienvenida():
    print("Bienvenido al programa usuario.")

for i in range(3):
    mostrarBienvenida()

print("=" * 40)
print("\n")

# EJERCICIO 2: Función con parámetros
# TODO: Crea una función 'calcular_area_rectangulo(base, altura)'
# TODO: Debe retornar el área (base * altura)
# TODO: Pruébala con diferentes valores

# Escribe tu código aquí:
def calcularAreaRectangulo(base, altura):
    return base * altura

base = float(input("Ingrese la base del rectangulo:"))
altura = float(input("Ingrese la altura del rectangulo:"))

resultado = calcularAreaRectangulo(base, altura)
print(f"El area del rectangulo es {resultado}")
print("=" * 40)
print("\n")

# EJERCICIO 3: Función con múltiples returns
# TODO: Crea una función 'analizar_numero(num)' que retorne:
#       - Si es par o impar (booleano)
#       - Si es positivo o negativo (string)
#       - Su valor absoluto (número)
# TODO: Pruébala con -15 y 8

# Escribe tu código aquí:
def analizar_numero(num):
    es_par = num % 2 == 0
    tipo = "positivo" if num >= 0 else "Negativo"
    absoluto = abs(num)
    return es_par, tipo, absoluto

numero = int(input("Ingrese un numero:"))
par, tipo, absoluto = analizar_numero(numero)
print(f"Par: {par}, Tipo: {tipo}, Absoluto: {absoluto}")
print("=" * 40)
print("\n")

# EJERCICIO 4: Función con valor por defecto
# TODO: Crea una función 'calcular_promedio(nota1, nota2, nota3, nota4=0)'
# TODO: Si no se pasa nota4, debe usar 0
# TODO: Retorna el promedio de las 4 notas

# Escribe tu código aquí:
def calcular_promedio( nota1, nota2, nota3, nota4=0):
    return (nota1+nota2+nota3+nota4) / 4

nota1 = float(input("Ingrese la primera nota:"))
nota2 = float(input("Ingrese la segunda nota:"))
nota3 = float(input("Ingrese la tercera nota:"))
nota4 = float(input("Ingrese la cuarta nota:"))

resultado2 = calcular_promedio(nota1, nota2, nota3, nota4)
print(f"El promedio de tus notas son: {resultado2}")
print("=" * 40)
print("\n")

# EJERCICIO 5: Convertir a función
# TODO: Convierte tu código del cajero automático en funciones
# Crea estas funciones:
# - consultar_saldo(saldo)
# - depositar(saldo, monto)
# - retirar(saldo, monto)
# Cada función debe retornar el nuevo saldo

# Escribe tu código aquí:
saldo = 100.00

def consultar_saldo(saldo):
    print(f"Saldo actual: S/{saldo:.2f}")
    return saldo

def depositar(saldo, monto):
    nuevoSaldo = saldo + monto
    print(f"Deposito exitoso. Nuevo saldo: S/{nuevoSaldo:.2f}")
    return nuevoSaldo

def retirar(saldo, monto):
    nuevoSaldo = saldo - monto
    print(f"Retiro exitoso. Nuevo saldo: S/{nuevoSaldo:.2f}")
    return nuevoSaldo
while True:
    print(f"====Menu====")
    print(f"1. Consultar saldo")
    print(f"2. Depositar saldo")
    print(f"3. Retirar saldo")
    print(f"4. Salir")
    opc = int(input("Ingrese una opcion:"))

    if opc == 1:
        consultar_saldo(saldo)
    elif opc == 2:
        monto = float(input("Ingrese el monto a depositar:"))
        depositar(saldo, monto)
    elif opc == 3:
        retiro = float(input("Ingrese el monto a retirar:"))
        retirar(saldo, retiro)
    elif opc == 4:
        print("Saliendo del menu.....")
        print("\n")
        break
    else:
        print("Opcion invalida")
print("=" * 40)
print("\n")

# EJERCICIO 6: Validador de edad
# TODO: Crea una función 'es_mayor_edad(edad)' que retorne True/False
# TODO: Crea una función 'categoria_edad(edad)' que retorne:
#       - "Niño" (0-12)
#       - "Adolescente" (13-17)
#       - "Adulto" (18-64)
#       - "Adulto mayor" (65+)

# Escribe tu código aquí:

def es_mayor_edad(edad):
    return edad >= 18

def categoria_edad(edad):
    if edad <= 12:
        return "NIño"
    elif edad <= 17:
        return "Adolescente"
    elif edad <= 64:
        return "Adulto"
    elif edad >= 65:
        return "Adulto mayor"

edad = int(input("Ingrese su edad:"))

esMayor = es_mayor_edad(edad)
categoria = categoria_edad(edad)

print(f"¿Eres Mayor?: {esMayor}")
print(f"Estas en la categoria de:{categoria}")
print("=" * 40)
print("\n")

# EJERCICIO 7: Calculadora con funciones
# TODO: Crea 4 funciones: sumar, restar, multiplicar, dividir
# TODO: Cada una recibe 2 números y retorna el resultado
# TODO: En dividir, valida que el divisor no sea 0

# Escribe tu código aquí:

def sumar( a, b ):
    return a + b

def restar(a , b):
    return a - b

def multiplicacion(a, b):
    return a * b

def dividir(a , b):
    if b == 0:
        print("Numero invalido")
    
    return a / b

print("====Calculadora====")
numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("Ingrese el segundo numero:"))

s = sumar(numero1, numero2)
r = restar(numero1, numero2)
m = multiplicacion(numero1, numero2)
d = dividir(numero1, numero2)

print("===Resultado====")
print(f"Suma: {s}")
print(f"Resta: {r}")
print(f"Multiplicacion: {m}")
print(f"Division: {d}")
print("=" * 40)
print("\n")

# EJERCICIO 8: Función lambda
# TODO: Crea una lambda que calcule el cubo de un número
# TODO: Usa map() para aplicarla a la lista [1, 2, 3, 4, 5]
# TODO: Imprime los resultados

# Escribe tu código aquí:
cubo = lambda x: x ** 3
numeros = [1,2,3,4,5]
cubos = list(map(cubo, numeros))
print(cubos)
print("=" * 40)
print("\n")

# EJERCICIO 9: Función recursiva (DESAFÍO)
# TODO: Crea una función 'factorial(n)' que calcule n!
# Ejemplo: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# Pista: factorial(n) = n * factorial(n-1)
#        factorial(1) = 1

# Escribe tu código aquí:
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

numero3 = int(input("Ingrese un numero para la factorial:"))
resultado3 = factorial(numero3)
print(f"Factorial: {resultado3}")
print("=" * 40)
print("\n")

# EJERCICIO 10: Validar contraseña (función completa)
# TODO: Crea una función 'validar_contraseña(password)' que retorne True si:
#       - Tiene al menos 8 caracteres
#       - Tiene al menos un número
#       - Tiene al menos una letra mayúscula
# TODO: Pruébala con: "hola123", "Python123", "python"

# Escribe tu código aquí:

contraseña = "Python123"

def validar_contraseña(password):
    if len(password) < 8:
        return False
    
    tiene_numero = any(c.isdigit() for c in password)
    tiene_mayuscula = any(c.isupper() for c in password)
    return tiene_numero and tiene_mayuscula

contraseña1 = "hola123"

resultado4 = validar_contraseña(contraseña1)
print(f"Valida la contraseña? {resultado4}")
print("=" * 40)
print("\n")