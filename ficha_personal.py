# PROYECTO: Crear una ficha personal interactiva

# Pedir datos al usuario
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuánto mides en metros? (ej: 1.75) "))
ciudad = input("¿En qué ciudad vives? ")
color = input("¿Que color te gusta? ")
estado = input("¿Estado civil? ")


# Calcular datos adicionales
edad_en_meses = edad * 12
altura_en_cm = altura * 100

# Mostrar la ficha
print("\n" + "="*40)
print("FICHA PERSONAL")
print("="*40)
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años ({edad_en_meses} meses)")
print(f"Altura: {altura} m ({altura_en_cm} cm)")
print(f"Ciudad: {ciudad}")
print(f"Color: {color} ")
print(f"Estado: {estado} ")
print("="*40)