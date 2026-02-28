# ============================================
# EJERCICIO 1: Calculadora Basica
# ============================================
# Objetivo: Practicar input(), conversion de tipos y operaciones aritmeticas.
#
# Instrucciones:
# - Completa las lineas marcadas con "___" para que el programa funcione.
# - El programa debe pedir dos numeros al usuario y mostrar
#   la suma, resta, multiplicacion y division de ambos.
# - Recuerda: input() devuelve un STRING, debes convertirlo a numero.
#
# Resultado esperado (ejemplo):
#   Ingrese el primer numero: 10
#   Ingrese el segundo numero: 3
#   Suma: 13.0
#   Resta: 7.0
#   Multiplicacion: 30.0
#   Division: 3.33
# ============================================

# Paso 1: Pedir el primer numero al usuario y convertirlo a decimal (float)
num1 = ___(input("Ingrese el primer numero: "))

# Paso 2: Pedir el segundo numero al usuario y convertirlo a decimal (float)
num2 = ___(___("Ingrese el segundo numero: "))

# Paso 3: Realizar las cuatro operaciones basicas
suma = num1 ___ num2          # Operador de suma
resta = num1 ___ num2         # Operador de resta
multiplicacion = num1 ___ num2  # Operador de multiplicacion
division = num1 ___ num2       # Operador de division

# Paso 4: Mostrar los resultados
# Usa f-strings para imprimir cada resultado
print(f"Suma: {suma}")
print(f"Resta: {___}")
print(f"Multiplicacion: {___}")
# Paso 5: Muestra la division con solo 2 decimales usando :.2f
print(f"Division: {division___}")
