# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora. 

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

# pido dia y horario al usuario
dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (formato hh:mm): ")
fecha = (dia, hora) # los estructuro en una tupla para buscarlos

# si la tumpla que ingresa el usuario está en la agenda, le muestro la actividad
if fecha in agenda:
    print(f"\nTenés actividades programadas: {agenda[fecha]}")
else:
    print("\nNo tenés activades programadas para ese dia y horario.")