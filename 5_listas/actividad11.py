# 11) Crear una lista con los nombres de 10 estudiantes.
# ● Solicitar al usuario que ingrese un nombre a buscar.
# ● Indicar si el nombre se encuentra en la lista.
# ● Mostrar la posición en la que aparece.
# ● Si no se encuentra, informar que no está en la lista

estudiantes = ["Ana", "Matias", "Clara", "Nicolas", "Romina", "Juan", "Josefina", "Felipe", "Pedro", "Lucia"]

nombre = input("Ingrese un nombre a buscar: ").capitalize() # para que ingrese con 1ra letra mayuscula

encontrado = False # bandera

# recorro la lista de estudiantes
for i in range(len(estudiantes)):
    if estudiantes[i] == nombre: # busco uno por uno al que coincida con el nombre ingrresado
        print("El nombre está en la lista")
        print("Posición:", i)
        encontrado = True # paso la bandera a True y corto el bucle una vez que se lo encuentra
        break

if encontrado == False: # si no lo encuentra dejo la bandera en False y envio aviso al usuario
    print("El nombre no está en la lista")