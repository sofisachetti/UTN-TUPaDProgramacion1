'''
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique
'''

def fibonacci(num):
    if num == 0:  # defino los casos base
        return 0
    elif num == 1:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2) # recursividad: como c/ num es la suma de los dos anteriores, calculo en la función el num - 1 y se lo sumo al num - 2

posicion = int(input("Ingrese una posición: "))  # pido al usuario un numero entero
for i in range(posicion + 1):  # con for recorro las posiciones
    print(fibonacci(i), end=" ")  # imprimo el resultado, con espacios entre cada uno