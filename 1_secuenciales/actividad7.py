# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print('------ EJERCICIO 7 ------\n')

numeroA = int(input('Ingrese el primer número: '))
numeroB = int(input('Ingrese el segundo número: '))
if numeroA != 0 and numeroB != 0: 
    print(f'Suma: {numeroA} + {numeroB} = {numeroA + numeroB}')
    print(f'Resta: {numeroA} - {numeroB} = {numeroA - numeroB}')
    print(f'División: {numeroA} / {numeroB} = {numeroA / numeroB}')
    print(f'Multiplicación: {numeroA} x {numeroB} = {numeroA * numeroB}')
else:
    print('Error. Los números ingresados deben ser distintos de 0.')
