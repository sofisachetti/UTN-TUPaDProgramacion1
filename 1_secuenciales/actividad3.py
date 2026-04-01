# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

print('------ EJERCICIO 3 ------\n')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
residencia = input('Ingrese su lugar de residencia: ')
print(f'Hola! Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.')