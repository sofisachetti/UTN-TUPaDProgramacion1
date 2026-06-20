'''
Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario.
'''

# ejemplos
# factorial de 5 = 5 x 4 x 3 x 2 x 1 = 120  ->  la recursividad la veo en 5x4 | 4x3 | 3x2 | 2x1 
# factorial de 4 = 4 x 3 x 2 x 1 = 24
# factorial de 3 = 3 x 2 x 1 = 6
# cuando se llega a 1x1 = 1 y 1x0 = 1  -> es el caso base y se corta ahí

def factorial(num):
    if num == 1:   # acá defino el caso base
        return 1
    else:
        return num * factorial(num - 1)  # recursividad: numero * factorial del número menos uno

numero = int(input("Ingrese un número entero para calcular los factoriales: "))  # pido al usuario un numero entero
for i in range(1, numero + 1):   # con for se recorre el rango del num ingresado por el usuario
    print(f"Factorial de {i}: {factorial(i)}")  # imprime el factorial de cada uno de los números
