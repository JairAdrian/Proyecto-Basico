# EJERCICIO 1: Listas - Gestión de tareas
# TODO: Crea una lista vacía de tareas
# TODO: Agrega 3 tareas con append()
# TODO: Inserta una tarea urgente al inicio con insert()
# TODO: Elimina la segunda tarea con pop()
# TODO: Ordena las tareas alfabéticamente
# TODO: Muestra la lista final

# Escribe tu código aquí:
tareas = []
tareas.append("Estudiar python")
tareas.append("Hacer gelatinas")
tareas.append("Hacer ejercicio")
tareas.insert(0, "Urgente: Salir a vender")
tareas.pop(1)
tareas.sort()
print("====Tareas====")
print(tareas)
print("=" * 40)
print("\n")

# EJERCICIO 2: List Comprehension
# TODO: Crea una lista con los números del 1 al 20
# TODO: Usa list comprehension para crear una lista con solo los múltiplos de 3
# TODO: Usa list comprehension para crear una lista con los cuadrados de números pares

# Escribe tu código aquí:
numeros = list(range(1,21))
multiplos_3 = [n for n in numeros if n % 3 == 0]
cuadrados_pares = [n**2 for n in numeros if n % 2 == 0]
print("====Numeros comprehension====")
print(f"Multiplos de 3: {multiplos_3}")
print(f"Cuadrados de pares: {cuadrados_pares}")
print("=" * 40)
print("\n")

# EJERCICIO 3: Diccionario - Agenda de contactos
# TODO: Crea un diccionario con 3 contactos (nombre: teléfono)
# TODO: Agrega 2 contactos más
# TODO: Modifica el teléfono de un contacto
# TODO: Elimina un contacto
# TODO: Muestra todos los nombres
# TODO: Muestra todos los teléfonos
# TODO: Muestra nombre y teléfono de cada uno

# Escribe tu código aquí:
print("====Agenda de Contactos====")
agenda = {"Ana": "9123", "Luis" : "9543", "Marcos" : "9512"}
agenda["Maria"] = "9451"
agenda["Carla"] = "9945"
agenda["Luis"] = "9999"
del agenda["Maria"]
print(f"Nombres: {list(agenda.keys())}")
print(f"Telefonos: {list(agenda.values())}")
for nombre, telefono in agenda.items():
    print(f"{nombre} : {telefono}")
print("=" * 40)
print("\n")

# EJERCICIO 4: Sets - Eliminar duplicados
# TODO: Crea una lista con números duplicados: [1, 2, 2, 3, 4, 4, 4, 5]
# TODO: Conviértela a set para eliminar duplicados
# TODO: Vuelve a convertir a lista
# TODO: Imprime la lista sin duplicados

# Escribe tu código aquí:
print("====Numeros Duplicados====")
lista_duplicados = [1,2,3,3,4,4,5]
sin_duplicados = list(set(lista_duplicados))
print(f"Sin duplicados: {sin_duplicados}")
print("=" * 40)
print("\n")

# EJERCICIO 5: Tuplas - Coordenadas
# TODO: Crea 3 tuplas con coordenadas (x, y)
# TODO: Guárdalas en una lista
# TODO: Recorre la lista e imprime cada coordenada desempaquetada

# Escribe tu código aquí:
print("====Coordenadas====")
coord1 = (12, 20)
coord2 = (10, 30)
coord3 = (15, 25)
coordenadas = [coord1, coord2, coord3]
for x, y in coordenadas:
    print(f"x= {x} , y= {y}")
print("=" * 40)
print("\n")

# EJERCICIO 6: Strings - Análisis de texto
# TODO: Pide al usuario una frase
# TODO: Cuenta cuántas palabras tiene (usa split())
# TODO: Cuenta cuántas vocales tiene
# TODO: Convierte todo a mayúsculas
# TODO: Reemplaza los espacios por guiones
# TODO: Muestra los resultados

# Escribe tu código aquí:
print("====Analisis de texto====")
frase = input("Ingrese una frase:")
palabras = len(frase.split())
vocales = sum(1 for c in frase.lower() if c in "aeiou")
mayusculas = frase.upper()
con_guiones = frase.replace(" ", "-")
print(f"Palabras = {palabras}")
print(f"Vocales = {vocales}")
print(f"Mayusculas = {mayusculas}")
print(f"Con guiones: {con_guiones}")
print("=" * 40)
print("\n")

# EJERCICIO 7: Diccionario - Inventario mejorado
# TODO: Crea un diccionario donde:
#       clave = nombre del producto
#       valor = otro diccionario con {"cantidad": X, "precio": Y}
# TODO: Agrega 3 productos
# TODO: Muestra el inventario completo
# TODO: Calcula el valor total del inventario (cantidad * precio de cada producto)

# Escribe tu código aquí:
print("====Inventario====")
inventario= {
    "Piña": {"Cantidad" : 10, "Precio": 3.40},
    "Gelatina": {"Cantidad": 20, "Precio": 3.00},
    "Vasos": {"Cantidad": 14, "Precio": 2.00},
}

for producto, datos in inventario.items():
    print(f"  {producto}: {datos['Cantidad']} unidades a S/.{datos['Precio']}")
total = sum(d["Cantidad"] * d["Precio"] for d in inventario.values())
print(f"Valor total del inventario: S/.{total:.2f}")
print("=" * 40)
print("\n")

# EJERCICIO 8: List + Dict - Estudiantes
# TODO: Crea una lista de diccionarios de estudiantes
# Cada estudiante tiene: nombre, edad, notas (lista de 4 notas)
# TODO: Calcula el promedio de cada estudiante
# TODO: Encuentra al estudiante con mayor promedio

# Escribe tu código aquí:
estudiantes = [
    {"Nombre": "Adrian", "Edad": 20, "Notas": [12, 14, 16, 15]},
    {"Nombre": "Maria", "Edad": 18, "Notas": [14,15,15,16]},
    {"Nombre": "Julian", "Edad": 19, "Notas": [13,12,14,15]}
]

for est in estudiantes:
    est["Promedio"] = sum(est["Notas"]) / len(est["Notas"])
    print(f"{est['Nombre']} : promedio {est['Promedio']:.1f}")
mejor = max(estudiantes, key=lambda e: e["Promedio"])
print(f"Mejor promedio: {mejor['Nombre']} con {mejor['Promedio']:.1f}")
print("=" * 40)
print("\n")
