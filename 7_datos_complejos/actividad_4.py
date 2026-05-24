# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 

# Inicializo un diccionario vacio para ir alamacenando los contactos
agenda_contactos = {}

# Con bucle for le pido al usuario los 5 contactos
for i in range(5):
    print(f"\nContacto {i + 1}: ")
    nombre = input("Ingrese el nombre: ").capitalize()
    numero = input("Ingrese el número: ")
    agenda_contactos[nombre] = numero

print(agenda_contactos)

# Pido al usuario el nombre a buscar
buscar_contacto = input("\nIngrese el nombre del contacto a buscar: ").capitalize()

# Busco con un condicional: si está muestro el número, sino aviso que el contacto no está en la agenda
if buscar_contacto in agenda_contactos:
    print(f"El número de {buscar_contacto} es: {agenda_contactos[buscar_contacto]}")
else:
    print("No existe ese contacto en la agenda.")