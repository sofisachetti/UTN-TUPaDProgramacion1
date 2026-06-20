'''
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
'''

def suma_digitos(num):
    if num < 10:  # caso base: si el numero tiene menos de dos cifras, entonces no se puede sumar y solo se devuelve el num
        return num
    
    return (num % 10) + suma_digitos(num // 10)   # como se trabaja con decimal se divide x 10, se suma el resto mas el resultado entero
#ej 15:  15%10=5  +  15//10=1  =  6

numero = int(input("Ingrese un número: "))
print("Suma de los digitos: ", suma_digitos(numero))