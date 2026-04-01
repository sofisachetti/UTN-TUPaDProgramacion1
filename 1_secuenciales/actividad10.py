# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

print('------ EJERCICIO 10 ------\n')

numero1 = int(input('Ingrese el primer número: '))
numero2 = int(input('Ingrese el segundo número: '))
numero3 = int(input('Ingrese el tercer número: '))
promedio = (numero1 + numero2 + numero3) / 3
print(f'El promedio de los números {numero1}, {numero2}, {numero3} es de {promedio}.')