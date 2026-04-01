# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

print('------ EJERCICIO 4 ------\n')

radio = int(input('Ingrese el radio del círculo: '))
areaCirculo = 3.14 * (radio ** 2)
perimetroCirculo = 2 * 3.14 * radio
print(f'El área del círculo es de: {areaCirculo}\nSu perímetro es de: {round(perimetroCirculo)}')