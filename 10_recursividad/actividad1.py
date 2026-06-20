'''
Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario.
'''

def factorial(num):
    if num == 1:   # acá defino el caso base
        return 1
    else:
        return num * factorial(num - 1)  # recursividad: numero * factorial del número menos uno

numero = int(input("Ingrese un número entero para calcular los factoriales: "))  # pido al usuario un numero entero
for i in range(1, numero + 1):   # con for se recorre el rango del num ingresado por el usuario
    print(f"Factorial de {i}: {factorial(i)}")  # imprime el factorial de cada uno de los números
