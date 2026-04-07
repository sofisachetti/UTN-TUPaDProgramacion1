# 12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
# ● Mostrar la lista original.
# ● Mostrar la lista ordenada de menor a mayor.
# ● Mostrar la lista ordenada de mayor a menor.
# ● Investigar el uso de sorted() y del parámetro reverse.

numeros = []

# pido los numeros con un bucle for, limitado en 8
for i in range(8):
    num = int(input("Ingrese un número entero: ")) # paso el input a int
    numeros.append(num) # lo voy almacenando en la lista

# original
print("Lista original:", numeros)

# de menor a mayor. sorted() -> ordena la lista y devuelve una nueva, por defecto es asc o alfabeticamente a-z
orden_asc = sorted(numeros)
print("Orden ascendente:", orden_asc)

# de mayor a menos
orden_desc = sorted(numeros, reverse=True) # si aplico reverse=True indico que el sorten sería al revés, en orden desc.
print("Orden descendente:", orden_desc)