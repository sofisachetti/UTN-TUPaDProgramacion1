# 1) Crear una lista con las notas de 10 estudiantes.
# ● Mostrar la lista completa.
# ● Calcular y mostrar el promedio.
# ● Indicar la nota más alta y la más baja.


# lista de notas
notas = [9, 4, 10, 6, 7, 9, 5, 8, 7, 3]


# mostrar lista completa, con bucle for para que las muestre de a una
print("Lista de notas: ")
for i in notas:
    print(i)


# calcular y mostrar el promedio
suma = 0 # inicio la suma en 0
for i in notas:
    suma += i  # con cada iteracion agrego a suma un valor
promedio = suma / len(notas) # con el total de las notas sumadas las divido por la longitud de la lista
print(f"\nEl promedio de notas es de: {promedio}")


# indicar la nota mas alta y la mas baja
# lo puedo hacer con los metodos integrados en python (que seria lo mas eficiente)
menor = min(notas)
mayor = max(notas)
print("\nCon funciones de Python:")
print(f"La nota más baja es: {menor}, mientras que la nota más alta es: {mayor}.")

# o tambien se puede hacer con un bucle for
minimo = notas[0] # comienzo con el primer numero de la lista tanto para el min como el max
maximo = notas[0]
for nota in notas: # bucle for así recorro la lista una sola vez 
    if nota < minimo: 
        minimo = nota # si la nota es mas chica que la almacenada entonces la asigno al minimo
    if nota > maximo:
        maximo = nota # si la nota es mas grande que la almacenda entonces la asigno al maximo
print("\nCon bucle for:")
print(f"La nota más baja es: {minimo} y la nota más alta es: {maximo}")