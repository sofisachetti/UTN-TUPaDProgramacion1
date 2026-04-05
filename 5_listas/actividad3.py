# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# ● Crear una lista con los pares y otra con los impares.
# ● Mostrar cuántos números tiene cada lista.

# uso el modulo random para generar los numeros al azar
import random

lista = [random.randint(1, 100) for i in range(15)] # limito el rango (numeros entre 1 y 100) y con el for establezco la cantidad de numeros
print("Lista de numeros al azar: ", lista)

# inicializo listas para pares e impares
pares = []
impares = []

# recorro la lista y separo los pares de los impares, guaradondolos en la lista correspondiente
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# imprimo ambas listas
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")