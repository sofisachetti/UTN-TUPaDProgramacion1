# Dada una lista con valores repetidos:
# ● Crear una nueva lista sin elementos repetidos.
# ● Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# inicializo lista de sin repetidos vacia
sin_repetidos = []

for num in datos: # bucle for para ir iterando la lista datos
    if num not in sin_repetidos: # si el num no esta en la lista sin_repetir lo agrego, si ya está sigue el bucle
        sin_repetidos.append(num)

print(f"Lista original: {datos}")
print(f"Lista sin numeros repetidos: {sin_repetidos}")