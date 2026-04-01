# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

print('------ EJERCICIO 5 ------\n')

segundos = int(input('Ingrese la cantidad de segundos: '))
minutos = segundos // 60
horas = minutos // 60
print(f'Los segundos ingresados equivalen a {horas} horas.')