# EJERCICIO 1: Par o Impar con IF
# TODO: Pide un número al usuario
# TODO: Usa if-else para determinar si es par o impar
# TODO: Imprime el resultado

# Escribe tu código aquí:
print(f"====Calcular Par o Impar====")
numero1 = int(input("Ingrese el numero:"))
if numero1 % 2 == 0:
    print(f"El numero {numero1} es par")
else:
    print(f"El numero {numero1} es impar")
print("=" * 40)

# EJERCICIO 2: Calculadora de notas mejorada
# TODO: Pide una nota (0-20)
# TODO: Usa if-elif-else para clasificar:
#       - 18-20: Excelente
#       - 15-17: Bueno
#       - 13-14: Regular
#       - 11-12: Deficiente
#       - 0-10: Desaprobado
# TODO: Imprime la clasificación

# Escribe tu código aquí:
print(f"\n" + "=" * 40)
print(f"====Sistema de Notas====")
nota1 = float(input("Ingrese la nota:"))
if nota1 >= 18:
    print("Clasificación: Excelente:")
elif nota1 >= 15:
    print("Clasificación: Bueno:")
elif nota1 >= 13:
    print("Clasificación: Regular:")
elif nota1 >= 11:
    print("Clasificación: Deficiente:")
elif nota1 >= 0:
    print("Clasificación: Desaprobado:")
print("=" * 40)

# EJERCICIO 3: Descuento en tienda
# Una tienda tiene estas reglas:
# - Si compras más de $200: 20% descuento
# - Si compras entre $100 y $200: 10% descuento
# - Si compras menos de $100: sin descuento
#
# TODO: Pide el monto de compra
# TODO: Calcula el descuento según las reglas
# TODO: Muestra el monto final a pagar

# Escribe tu código aquí:
print(f"\n" + "=" * 40)
print(f"====SuperMarket====")
monto = float(input("Ingrese el monto a comprar:"))
if monto >= 200:
    print(f"Por haber tenido un monto de S/{monto}")
    print(f"Recibira un descuento del 20%")
    descuento = monto * 0.20
    print(f"Solo pagara S/{descuento}")
elif monto >= 100:
    print(f"Por haber tenido un monto de S/{monto}")
    print(f"Recibira un descuento del 10%")
    descuento = monto * 0.10
    print(f"Solo pagara S/{descuento}")
elif monto >= 0:
    print(f"Por haber tenido un monto de S/{monto}")
    print(f"No pudo recibir un descuento")
print("=" * 40)

# EJERCICIO 4: Verificador de edad para cine
# El cine tiene estas categorías:
# - Menores de 5: Gratis
# - 5-12 años: Entrada niño ($5)
# - 13-17 años: Entrada adolescente ($8)
# - 18-64 años: Entrada adulto ($12)
# - 65 o más: Entrada adulto mayor ($6)
#
# TODO: Pide la edad
# TODO: Determina el precio según la edad
# TODO: Muestra el tipo de entrada y el precio

# Escribe tu código aquí:
print(f"\n" + "=" * 40)
print(f"=====CinePlanet=====")
edad = int(input("Ingrese su edad:"))

if edad <= 5:
    print(f"Tendras una entrada gratis")
elif edad >= 5:
    print(f"La entrada te costara S/5")
elif edad >= 13:
    print(f"La entrada te costara S/8")
elif edad >= 18:
    print(f"La entrada te costara S/12")
elif edad >= 65:
    print(f"La entrada te costara S/6")
print("=" * 40 )

# EJERCICIO 5: Validador de contraseña
# Una contraseña es segura si cumple:
# - Tiene 8 o más caracteres
# - (Para este ejercicio, asume que tiene números y letras)
#
# TODO: Pide una contraseña al usuario
# TODO: Valida la longitud
# TODO: Si es válida: "Contraseña segura"
# TODO: Si no: "Contraseña débil, debe tener al menos 8 caracteres"

# Escribe tu código aquí:
print(f"\n" + "=" * 40)
print(f"====Validar Contraseña====")
contraseña = input("Ingrese su contraseña:")

if len(contraseña) >= 8:
    print(f"La contraseña es muy segura.")
else:
    print(f"La contraseña no tiene 8 digitos")
print("=" * 40)

# EJERCICIO 6: Día de la semana
# TODO: Pide al usuario un día de la semana
# TODO: Usa if-elif para determinar si es:
#       - Lunes a Viernes: "Día laboral"
#       - Sábado o Domingo: "Fin de semana"
# PISTA: Usa el operador 'in' con una lista

# Escribe tu código aquí:
print(f"\n" + "=" * 40)
print(f"====Dia de la Semanas====")
dia = input("Ingrese el dia de hoy:")

if dia in ["Lunes", "Martes", "Miercoles", "Jueves", "Vienes"]:
    print(f"Dia Laboral")
elif dia in ["Sabado", "Domingo"]:
    print(f"Fin de Semana")
print("=" * 40)

# EJERCICIO 7: Sistema de login simple
# TODO: Define un usuario correcto: "admin"
# TODO: Define una contraseña correcta: "python123"
# TODO: Pide al usuario que ingrese usuario y contraseña
# TODO: Valida si ambos son correctos
# TODO: Muestra "Acceso concedido" o "Acceso denegado"

# Escribe tu código aquí:
print(f"\n" + "=" * 40)

usuarioAdmin = "admin"
contraseñaAdmin = "python123"

usuario = input("Ingrese su Usuario:")
contraseña1 = input("Ingrese su contraseña:")

if usuario == usuarioAdmin and contraseña == contraseñaAdmin:
    print(f"Acceso Adminstrador valido.")
else:
    print(f"Acceso denegado")