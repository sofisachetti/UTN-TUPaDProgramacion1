# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.

print('------ EJERCICIO 8 ------\n')

altura = float(input('Ingrese su altura en metros: '))
peso = float(input('Ingrese su peso en kilogramos: '))
imc = peso / (altura) ** 2
print(f'Segun la altura ({altura} mts.) y el peso ({peso} kg.), su índice de masa corporal es de: {round(imc)}.')