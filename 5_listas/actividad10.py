# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# ● Mostrar el total vendido por cada producto.
# ● Mostrar el día con mayores ventas totales.
# ● Indicar cuál fue el producto más vendido en la semana.

# filas = productos / columnas = cant vendida x dia
ventas = [
    [10, 12, 8, 9, 11, 7, 6],
    [5, 7, 6, 8, 7, 9, 10],
    [15, 14, 13, 12, 11, 10, 9],
    [8, 9, 7, 6, 5, 4, 3]
]

# total vendido x producto -> sumar por fila
# recorro la longitud del array principal 
for i in range(len(ventas)):
    total = sum(ventas[i]) # sumo los elementos dentro de cada sub lista
    print(f"Total producto {i + 1}: {total}")

# dia con mayores ventas -> sumar por columnas
mayor_total = 0 # inicializo variables para acumular
mayor_dia = 0
for i in range(len(ventas[0])): # recorro la cantidad de dias
    suma_dia = 0 # incializo la suma del dia
    for j in range(len(ventas)): # recorro el array principal
        suma_dia += ventas[j][i] # ventas[producto][venta x dia]

        if suma_dia > mayor_total:
            mayor_total = suma_dia
            mayor_dia = j
print(f"El dia con mayores ventas fue el {mayor_dia + 1}, con una cantidad total de {mayor_total}.")

#producto mas vendido de la semana -> por fila
mayor_venta = 0 # incializo variables
producto_mayor = 0

for i in range(len(ventas)): # recorro la lista por producto (fila)
    total = sum(ventas[i]) # almaceno en total la suma de todos los dias
    
    if total > mayor_venta: # comparo con la venta mayor
        mayor_venta = total
        producto_mayor = i
print(f"El producto más vendido es el {producto_mayor + 1}, con un total de {mayor_venta} unidades.")