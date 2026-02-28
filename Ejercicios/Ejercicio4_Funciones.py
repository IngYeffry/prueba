# ============================================
# EJERCICIO 4: Funciones - Conversor de Temperatura
# ============================================
# Objetivo: Practicar la creacion y uso de funciones (def, return, parametros).
#
# Instrucciones:
# - Completa las lineas marcadas con "___" para que el programa funcione.
# - Crea dos funciones:
#     * celsius_a_fahrenheit(celsius) --> retorna la conversion a Fahrenheit
#     * fahrenheit_a_celsius(fahrenheit) --> retorna la conversion a Celsius
#
# Formulas:
#   Fahrenheit = (Celsius * 9/5) + 32
#   Celsius = (Fahrenheit - 32) * 5/9
#
# Resultado esperado (ejemplo):
#   === CONVERSOR DE TEMPERATURA ===
#   1. Celsius a Fahrenheit
#   2. Fahrenheit a Celsius
#   Elija una opcion (1 o 2): 1
#   Ingrese la temperatura en Celsius: 100
#   100.0 °C equivale a 212.00 °F
# ============================================

# Paso 1: Definir la funcion que convierte de Celsius a Fahrenheit
# Usa la palabra clave 'def' para crear la funcion
___ celsius_a_fahrenheit(celsius):
    # Paso 2: Aplicar la formula y retornar el resultado
    resultado = (celsius ___ 9/5) + 32
    ___ resultado

# Paso 3: Definir la funcion que convierte de Fahrenheit a Celsius
___ fahrenheit_a_celsius(fahrenheit):
    # Paso 4: Aplicar la formula y retornar el resultado
    resultado = (___ - 32) * 5/9
    return ___

# === Programa principal ===
print("=== CONVERSOR DE TEMPERATURA ===")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = input("Elija una opcion (1 o 2): ")

if opcion == "1":
    # Paso 5: Pedir la temperatura en Celsius y convertirla a float
    temp = ___(input("Ingrese la temperatura en Celsius: "))
    # Paso 6: Llamar a la funcion celsius_a_fahrenheit pasando 'temp' como argumento
    resultado = ___(temp)
    # Paso 7: Mostrar el resultado con 2 decimales
    print(f"{temp} °C equivale a {resultado___} °F")

elif opcion == "2":
    temp = float(input("Ingrese la temperatura en Fahrenheit: "))
    # Paso 8: Llamar a la funcion fahrenheit_a_celsius
    resultado = ___(temp)
    print(f"{temp} °F equivale a {resultado:.2f} °C")

else:
    print("Opcion no valida. Debe elegir 1 o 2.")
