# EJERCICIO 1: Operadores Aritméticos
# TODO: Crea dos variables con números
# TODO: Realiza las 7 operaciones aritméticas (+, -, *, /, //, %, **)
# TODO: Imprime cada resultado con un mensaje descriptivo

# Escribe tu código aquí:
print(f"=====Calculadora de Operaciones======")
numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("Ingrese el segundo numero:"))
print ( f"La suma de los numeros: {numero1 + numero2 }")
print ( f"La resta de los numeros: {numero1 - numero2}")
print ( f"La multiplicacion de los numeros: {numero1 * numero2}")
print ( f"La division de los numeros: {numero1 / numero2}")
print ( f"La division sin decimales de los numeros: {numero1 // numero2}")
print ( f"La division de residuo de los numeros: {numero1 % numero2}")
print ( f"La potencia de los numeros: {numero1 ** numero2}")
print ("=" * 40)

# EJERCICIO 2: Calculadora de propina
# TODO: Crea una variable con el total de la cuenta (ej: 85.50)
# TODO: Crea una variable con el porcentaje de propina (ej: 15)
# TODO: Calcula cuánto es la propina
# TODO: Calcula el total a pagar (cuenta + propina)
# TODO: Imprime los resultados

# Escribe tu código aquí:
cuenta = float(input("Ingrese el total a pagar:"))
descuento = int(input("Ingrese el descuento:"))

propina = cuenta * descuento / 100
total = cuenta + propina
print (f"=======Resultado de Propina======")
print (f"Cuenta: ${cuenta}")
print (f"Propina ({descuento}%): ${propina}")
print (f"Total a pagar: {total}")
print ("=" * 40)

# EJERCICIO 3: Par o Impar
# TODO: Crea una variable con un número entero
# TODO: Usa el operador % para saber si es par o impar
# TODO: Guarda el resultado en una variable booleana
# Pista: Un número es par si numero % 2 == 0

# Escribe tu código aquí:
print(f"====Calculadora de par o impar======")
numero3 = int(input("Ingrese un numero:"))
par = numero3 % 2 == 0

print(f"====Resultado======")
print(f"El numero: {numero3} es par: {par}")
print("=" * 40)

# EJERCICIO 4: Comparaciones
# TODO: Crea dos variables con tu edad y la edad mínima para votar (18)
# TODO: Compara si tu edad es mayor o igual a 18
# TODO: Compara si tu edad es exactamente 18
# TODO: Compara si tu edad es diferente de 18
# TODO: Imprime los resultados

# Escribe tu código aquí:
print("====Calcuradora de Comparaciones=====")
edad = int(input("Ingrese su edad:"))
edadMax = 18
votar = edad >= edadMax
print(f"====Resultado=====")
print(f"Puedes votar: {votar}")
print("=" * 40)

# EJERCICIO 5: Operadores Lógicos - Sistema de Admisión
# Un estudiante puede ser admitido si:
# - Tiene promedio >= 14 Y asistencia >= 80%
# O
# - Es deportista destacado

# TODO: Crea variables: promedio, asistencia, es_deportista
# TODO: Crea una variable "es_admitido" con la lógica de arriba
# TODO: Imprime si es admitido o no

# Escribe tu código aquí:
print(f"====Sistema de Admisión====")
promedio = float(input("Ingrese el promedio de notas:"))
asistencia = int(input("Ingrese la cantidad de asistencia:"))
deportista = input("Es deportista o no? ( S / N ):")

if ( promedio >= 14 and asistencia >= 80  or deportista == "S"):
    print(f"Esta admitido")
else:
    print (f"No estas admitido")
print("=" * 40)

# EJERCICIO 6: Tienda Online
# Un cliente tiene envío gratis si:
# - Compra más de $50 O es cliente premium

# TODO: Crea variables: monto_compra, es_premium
# TODO: Determina si tiene envío gratis
# TODO: Imprime el resultado

# Escribe tu código aquí:

print(f"====Tienda Online====")
montoCompra = float(input("Ingrese el monto a comprar:"))
premium = input("Eres Premium ( S / N ):")

print(f"====Boleta====")
print(f"Monto a pagar: {montoCompra}")
if( montoCompra >= 250 or premium == "S"):
    print(f"Recibiras envio gratis")
else:
    print(F"Tendras que pagar extra por el envio")
print("=" * 40)


# EJERCICIO 7: Validación de Contraseña
# Una contraseña es válida si:
# - Tiene más de 8 caracteres Y contiene números

# TODO: Crea variables: contraseña = "python123", longitud_minima = 8
# TODO: Calcula la longitud con len(contraseña)
# TODO: Para este ejercicio, asume que tiene_numeros = True
# TODO: Valida si la contraseña es válida
# TODO: Imprime el resultado

# Escribe tu código aquí

contraseña = "adrianJair674"
logintudMin = 8
tieneNumeros = True

validarContraseña = len(contraseña) >= logintudMin and tieneNumeros

print(f"====Validacion Contraseña====")
print(f"Contraseña: {contraseña}")
print(f"Logintud: {len(contraseña)} caracteres")
print(f"Es valido?: {validarContraseña}")
print("=" * 40)