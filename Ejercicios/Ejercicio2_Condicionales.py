# ============================================
# EJERCICIO 2: Verificador de Edad
# ============================================
# Objetivo: Practicar condicionales (if, elif, else) y comparaciones.
#
# Instrucciones:
# - Completa las lineas marcadas con "___" para que el programa funcione.
# - El programa debe pedir la edad del usuario y clasificarlo en:
#     * Menor de 0 o mayor de 120 --> "Edad no valida"
#     * 0 a 12   --> "Eres un nino"
#     * 13 a 17  --> "Eres un adolescente"
#     * 18 a 64  --> "Eres un adulto"
#     * 65 a 120 --> "Eres un adulto mayor"
#
# Resultado esperado (ejemplo):
#   Ingrese su edad: 25
#   Eres un adulto
# ============================================

# Paso 1: Pedir la edad y convertirla a entero
edad = ___(input("Ingrese su edad: "))

# Paso 2: Evaluar la edad con condicionales
# Primero verificamos si la edad NO es valida (menor que 0 o mayor que 120)
if edad < 0 ___ edad > 120:
    print("Edad no valida")

# Si la edad esta entre 0 y 12 (inclusive)
___ edad <= 12:
    print("Eres un nino")

# Si la edad esta entre 13 y 17 (inclusive)
elif edad ___ 17:
    print("Eres un adolescente")

# Si la edad esta entre 18 y 64 (inclusive)
___ edad <= 64:
    print("Eres un adulto")

# Para cualquier otro caso (65 a 120)
___:
    print("Eres un adulto mayor")
