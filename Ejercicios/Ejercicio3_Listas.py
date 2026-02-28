# ============================================
# EJERCICIO 3: Lista de Compras
# ============================================
# Objetivo: Practicar listas, bucle while, y metodos de listas.
#
# Instrucciones:
# - Completa las lineas marcadas con "___" para que el programa funcione.
# - El programa permite al usuario agregar productos a una lista de compras.
# - El usuario escribe "salir" para terminar y ver la lista completa.
#
# Metodos utiles:
#   lista.append(elemento) --> agrega un elemento al final de la lista
#   lista.remove(elemento) --> elimina un elemento de la lista
#   len(lista)             --> devuelve cuantos elementos tiene la lista
#   .lower()               --> convierte un string a minusculas
#
# Resultado esperado (ejemplo):
#   === LISTA DE COMPRAS ===
#   Escriba un producto (o 'salir' para terminar): Leche
#   Producto 'Leche' agregado.
#   Escriba un producto (o 'salir' para terminar): Pan
#   Producto 'Pan' agregado.
#   Escriba un producto (o 'salir' para terminar): salir
#
#   --- Tu lista de compras ---
#   1. Leche
#   2. Pan
#   Total de productos: 2
# ============================================

# Paso 1: Crear una lista vacia para guardar los productos
lista_compras = ___

print("=== LISTA DE COMPRAS ===")

# Paso 2: Crear un bucle que se repita mientras el usuario no escriba "salir"
# Usamos while True para un bucle infinito que se rompe con 'break'
while ___:
    # Paso 3: Pedir un producto al usuario
    producto = input("Escriba un producto (o 'salir' para terminar): ")

    # Paso 4: Si el usuario escribe "salir" (en cualquier combinacion de mayusculas/minusculas),
    # salimos del bucle con 'break'
    if producto.___() == "salir":
        ___

    # Paso 5: Agregar el producto a la lista usando .append()
    lista_compras.___(producto)
    print(f"Producto '{producto}' agregado.")

# Paso 6: Mostrar la lista completa usando un bucle for con enumerate
# enumerate() nos da el indice (posicion) y el valor de cada elemento
print("\n--- Tu lista de compras ---")
for i, prod in ___(lista_compras):
    # Recuerda: enumerate empieza en 0, sumamos 1 para mostrar desde 1
    print(f"{i + ___}. {prod}")

# Paso 7: Mostrar el total de productos usando len()
print(f"Total de productos: {___(lista_compras)}")
