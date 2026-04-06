# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# ● Mostrar el promedio de cada estudiante.
# ● Mostrar el promedio de cada materia.

# cada fila es un alumno, cada columna seria una materia
notas = [
    [7, 8, 6],
    [9, 7, 8],
    [6, 5, 7],
    [8, 9, 10],
    [7, 6, 8]
]

# para el promedio de cada alumno, recorro la longitud de la matriz
for n in range(len(notas)):
    promedio = sum(notas[n]) // len(notas[n]) # sumo el total de las notas en cada sub array y lo divido por la cantidad de notas
    print(f"Promedio del estudiante {n + 1}: {promedio}")

# para el promedio por materia primero defino la cantidad de materias que hay (serian 3)
cant_materias = len(notas[0])

for i in range(cant_materias): # recorro la cantidad de materias
    suma = 0 # por cada una de las materias comienzo un contador de suma
    for j in range(len(notas)): # recorro la matriz general
        suma += notas[j][i] # a suma le voy a ir agregando cada una de las notas
    promedio = suma / len(notas) # hago el promedio
    print(f"Promedio de la materia {i + 1}: {promedio}")