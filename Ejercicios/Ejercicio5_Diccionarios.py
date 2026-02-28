# ============================================
# EJERCICIO 5: Registro de Estudiantes con Diccionarios
# ============================================
# Objetivo: Practicar diccionarios, bucles for, y f-strings.
#
# Instrucciones:
# - Completa las lineas marcadas con "___" para que el programa funcione.
# - El programa registra estudiantes con su nombre y 3 notas,
#   calcula el promedio de cada uno y muestra si aprobo o reprobo.
#
# Conceptos clave:
#   diccionario = {"clave": valor}          --> crear un diccionario
#   diccionario["nueva_clave"] = valor      --> agregar una clave
#   sum(lista)                              --> suma todos los elementos
#   len(lista)                              --> cuenta los elementos
#   range(n)                                --> genera numeros de 0 a n-1
#
# Resultado esperado (ejemplo):
#   === REGISTRO DE ESTUDIANTES ===
#   Cuantos estudiantes desea registrar? 2
#
#   --- Estudiante 1 ---
#   Nombre: Ana
#   Nota 1: 4.5
#   Nota 2: 3.8
#   Nota 3: 4.0
#
#   --- Estudiante 2 ---
#   Nombre: Luis
#   Nota 1: 2.5
#   Nota 2: 3.0
#   Nota 3: 2.8
#
#   === RESULTADOS ===
#   Ana    | Notas: [4.5, 3.8, 4.0] | Promedio: 4.10 | APROBO
#   Luis   | Notas: [2.5, 3.0, 2.8] | Promedio: 2.77 | REPROBO
# ============================================

print("=== REGISTRO DE ESTUDIANTES ===")

# Paso 1: Pedir cuantos estudiantes se van a registrar
cantidad = ___(input("Cuantos estudiantes desea registrar? "))

# Paso 2: Crear una lista vacia donde guardaremos los diccionarios de cada estudiante
estudiantes = ___

# Paso 3: Usar un bucle for con range() para registrar cada estudiante
for i in ___(cantidad):
    print(f"\n--- Estudiante {i + 1} ---")

    # Paso 4: Pedir el nombre del estudiante
    nombre = input("Nombre: ")

    # Paso 5: Crear una lista vacia para guardar las 3 notas
    notas = []

    # Paso 6: Usar un bucle for para pedir 3 notas
    for j in range(___):
        # Pedir cada nota y convertirla a float
        nota = ___(input(f"Nota {j + 1}: "))
        # Agregar la nota a la lista de notas
        notas.___(nota)

    # Paso 7: Crear un diccionario con los datos del estudiante
    # El diccionario debe tener dos claves: "nombre" y "notas"
    estudiante = {
        "___": nombre,
        "___": notas
    }

    # Paso 8: Agregar el diccionario a la lista de estudiantes
    estudiantes.append(___)

# === Mostrar resultados ===
print("\n=== RESULTADOS ===")

# Paso 9: Recorrer la lista de estudiantes
for est in ___:
    # Paso 10: Calcular el promedio dividiendo la suma de notas entre la cantidad
    # Usa sum() para sumar y len() para contar
    promedio = ___(est["notas"]) / ___(est["notas"])

    # Paso 11: Determinar si aprobo o reprobo (aprobar = promedio >= 3.0)
    if promedio ___ 3.0:
        estado = "APROBO"
    else:
        estado = "REPROBO"

    # Paso 12: Mostrar los datos formateados
    # Completa el f-string con las claves correctas del diccionario
    print(f"{est['___']:<7}| Notas: {est['___']} | Promedio: {promedio:.2f} | {estado}")
