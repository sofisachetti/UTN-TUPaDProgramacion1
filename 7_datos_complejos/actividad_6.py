# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno. 

alumnos = {}

# Lógica para agregar alumnos y sus notas
for i in range(3):
    print(f"\nAlumno {i + 1}:")
    
    nombre = input("Ingrese el nombre: ").capitalize()
    nota_1 = float(input("Ingrese la 1° nota (del 1 al 10): "))
    nota_2 = float(input("Ingrese la 2° nota (del 1 al 10): "))
    nota_3 = float(input("Ingrese la 3° nota (del 1 al 10): "))
    
    tupla_notas = (nota_1, nota_2, nota_3) # Guardo las 3 notas en una tupla
    
    alumnos[nombre] = tupla_notas # Guardo el nobre y las notas en el diccionario


# Lógica para el promedio de cada uno
print("\nPromedios: ")
for nombre, notas in alumnos.items(): # Desestructuro nombre y notas del diccionario, recorro cada uno con el bucle for
    promedio = (notas[0] + notas[1] + notas[2]) / 3  # Calculo el promedio
    print(f"{nombre}: {promedio:.2f}")