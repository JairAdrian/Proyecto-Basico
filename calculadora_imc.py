# CALCULADORA DE IMC
# IMC = peso / (altura ** 2)
# Clasificación:
# - Bajo peso: IMC < 18.5
# - Normal: 18.5 <= IMC < 25
# - Sobrepeso: 25 <= IMC < 30
# - Obesidad: IMC >= 30

print("=== CALCULADORA DE IMC ===")

# Pedir datos
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calcular IMC
imc = peso / (altura ** 2)

# Clasificación
bajo_peso = imc < 18.5
normal = imc >= 18.5 and imc < 25
sobrepeso = imc >= 25 and imc < 30
obesidad = imc >= 30

# Mostrar resultados
print(f"\nTu IMC es: {imc:.2f}")
print(f"Bajo peso: {bajo_peso}")
print(f"Normal: {normal}")
print(f"Sobrepeso: {sobrepeso}")
print(f"Obesidad: {obesidad}")