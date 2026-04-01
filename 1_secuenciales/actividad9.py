# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. 

print('------ EJERCICIO 9 ------\n')

celsius = float(input('Ingrese la temperatura en Celsius: '))
fahr = (9/5 * celsius) + 32
print(f'El equivalente de {celsius} C° en Fahrenheit es de {fahr} F°.')
