# EJERCICIO 1: Crea variables con tu información personal
# TODO: Crea una variable con tu nombre (string)
# TODO: Crea una variable con tu edad (int)
# TODO: Crea una variable con tu altura en metros (float)
# TODO: Crea una variable que indique si eres estudiante (bool)

# Escribe tu código aquí:
nombre = "Adrian"
edad = 20
altura = 1.80
est = False



# EJERCICIO 2: Imprime tus variables
# TODO: Usa print() para mostrar cada variable
# Ejemplo: print("Mi nombre es:", nombre)

# Escribe tu código aquí:

print ( "Mi nombre es: " + nombre )
print ( "Mi edad es: ", edad )
print ( "Mi altura es: ", altura )
print ( "Estoy estudiando:", est )

# EJERCICIO 3: Conversiones
# TODO: Convierte tu edad a string y guárdala en una nueva variable
# TODO: Convierte tu altura a int (perderá los decimales)
# TODO: Imprime los tipos de dato con type()

# Escribe tu código aquí:
edadTexto = (str(edad))
alturaTexto = (str(altura))

print( "Tipos de datos")
print ( "Tipo de Edad: ", type(edad) )
print( "Tipo de edadTexto: ", type(edadTexto))
print( "Tipo de altura: ", type(altura))
print( "Tipo de alturaTexto: ", type(alturaTexto))

# EJERCICIO 4: Operaciones básicas con números
# TODO: Crea dos variables numéricas (pueden ser tu edad y la de un amigo)
# TODO: Suma ambas edades y guarda el resultado
# TODO: Multiplica tu edad por 2
# TODO: Imprime los resultados

# Escribe tu código aquí:
edadAmigo = 24
sumaEdad = edad + edadAmigo
multiEdad = edad * 2

print( "Suma de edades")
print( "Mi edad: ", edad)
print( "La edad de mi amigo: ", edadAmigo)
print( "Suma de las 2 edades: ", sumaEdad)
print( "Multiplicacion por 2 de mi edad: ", multiEdad)

# EJERCICIO 5: Concatenación de strings
# TODO: Crea variables con tu nombre y apellido
# TODO: Une (concatena) nombre y apellido en una nueva variable
# Pista: usa el operador +
# TODO: Imprime el nombre completo

# Escribe tu código aquí:

apellido = "Cienfuegos"

print( "Mi nombre completo es: " + nombre + " " + apellido)