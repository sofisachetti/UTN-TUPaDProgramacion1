# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

print('------ EJERCICIO 6 ------\n')
numeroTabla = int(input('Ingrese el número para la tabla de multiplicar: '))

# Esta sería la forma de hacerlo de manera secuencial:
print('\nSECUENCIAL: ')
print(f'1 x {numeroTabla} = {numeroTabla * 1}')
print(f'2 x {numeroTabla} = {numeroTabla * 2}')
print(f'3 x {numeroTabla} = {numeroTabla * 3}')
print(f'4 x {numeroTabla} = {numeroTabla * 4}')
print(f'5 x {numeroTabla} = {numeroTabla * 5}')
print(f'6 x {numeroTabla} = {numeroTabla * 6}')
print(f'7 x {numeroTabla} = {numeroTabla * 7}')
print(f'8 x {numeroTabla} = {numeroTabla * 8}')
print(f'9 x {numeroTabla} = {numeroTabla * 9}')
print(f'10 x {numeroTabla} = {numeroTabla * 10}')


# Resolucion con bucle for para evitarnos la repeticion:
print('\nCON for...in')
for i in range(1, 11):
    print(f'{i} x {numeroTabla} = {numeroTabla * i}')
