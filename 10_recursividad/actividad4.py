'''
Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
binario -> num dividido sucesivamente  por 2, se lee de abajo hacia arriba
'''

def decimal_a_binario(num):
    if num < 2:   # definicio de caso bas, cuando 
        return str(num)  # se va air almacenando como un string

    return decimal_a_binario(num // 2) + str(num % 2)  # recursividad: al resultado del num // 2, se le suma el modulo del num

numero = int(input("Ingrese un número decimal: "))
print("Binario:", decimal_a_binario(numero))