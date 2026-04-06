# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# ● Calcular el promedio de las mínimas y el de las máximas.
# ● Mostrar en qué día se registró la mayor amplitud térmica.

temp_semana = [
    [13, 17],
    [12, 19],
    [11, 22],
    [10, 21],
    [14, 23],
    [15, 25],
    [17, 24]
]

# para los promedios inicializo una sumatoria, tanto para minimas como maximas
sum_minimas = 0
sum_maximas = 0

# con bucle for recorro la matriz por fila (dia)
for dia in temp_semana:
    sum_minimas += dia[0] # sabemos que las temp en posicion 0 son las mas bajas y en posicion [1] son las mas altas, asi que las asignamos a cada sumatoria
    sum_maximas += dia[1]

# calculo el promedio a partir de la sumatoria de cada temp y lo divido por la cantidad de dias con len(temp_semana)
promedio_min = sum_minimas // len(temp_semana)
promedio_max = sum_maximas // len(temp_semana)

# variables para almacenar la mayor amplitud y el dia que la tenga
mayor_amplitud = 0
dia = 0

for i in range(len(temp_semana)): # recorro la lista segun su longitud
    amplitud = temp_semana[i][1] - temp_semana[i][0] # amplitud es la temperatura mas alta, menos la mas baja.
    if amplitud > mayor_amplitud: #si esa resta da mayor que la amplitud que tengo almacenda, la cambio
        mayor_amplitud = amplitud
        dia = i # guardo el indice del dia que tenga la mayor amplitud

print("Reporte de temperaturas:")
print(f"Promedio de temperaturas mínimas: {promedio_min} C°.")
print(f"Promedio de temperaturas máximas: {promedio_max} C°.")
print(f"La mayor amplitud térmica fue de {mayor_amplitud} C°, el día {dia + 1}.")