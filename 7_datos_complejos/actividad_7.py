# 7) Se recibe el registro diario de asistencia a una capacitación en forma de lista.
# En dicha lista pueden aparecer nombres repetidos, ya que una misma persona pudo haber asistido en más de una jornada.
# • Mostrá la lista original de asistencias.
# • Generá un conjunto (set) a partir de la lista y mostrar los empleados que asistieron al menos una vez (sin repetir nombres).
# • Indicá cuántas veces asistió cada empleado a la capacitación.

# Lista original
asistencias = ["Ana", "Luis", "Ana", "María", "Luis", "Pedro", "Ana"]
print("\nLista original: ")
print(asistencias)

# Set de las asistencias
asistencias_sin_repetir = set(asistencias)
print("\nLista de empleados que asistieron al menos una vez: ")
print(asistencias_sin_repetir)

# Logica para saber cuantas veces asistieron, misma que se aplicó en la actividad 5
cantidad_asistencias = {}

for i in asistencias:
    if i in cantidad_asistencias:
        cantidad_asistencias[i] += 1
    else:
        cantidad_asistencias[i] = 1

print("\nCantidad de veces que los empleados asistieron a la capacitación: ")
print(cantidad_asistencias)