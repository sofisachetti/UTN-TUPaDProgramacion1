# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# ● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# ● Mostrar la lista final actualizada.

estudiantes = ["Ana", "Matias", "Clara", "Nicolas", "Romina", "Juan", "Josefina", "Felipe"]

# menu de opciones 
opcion = input("Elija la acción que desea realizar:\n1- Agregar estudiante\n2- Eliminar estudiante\nOpcion (1 o 2): ")
opcion_validar = opcion.isdigit() # valido que el input sea un digito

# condicional para cada opcion
if opcion_validar and opcion == "1":
    nuevo_estudiante = input("\nIngrese el nombre del estudiante: ").capitalize() #uso capitalize para que el primer caracter sea mayuscula y el resto minuscula 
    estudiantes.append(nuevo_estudiante) # agrego el nuevo estudiante a la lista
    print("Estudiante agregado con exito!")
    print("\nLista de estudiantes actualizada: ") # muestro la lista actualizada
    for e in estudiantes:
        print(e)
elif opcion_validar and opcion == "2":
    estudiante_eliminar = input("Ingrese el nombre del estudiante a eliminar: ").capitalize() # pido el nombre del estudiante
    if estudiante_eliminar in estudiantes: # valido si el nombre esta en la lista
        estudiantes.remove(estudiante_eliminar) # elimino
        print("Estudiante eliminado con exito!")
        print("\nLista de estudiantes actualizada: ") # muestro la lista actualizada
        for e in estudiantes:
            print(e)
    else: # sino aviso que el estudiante no esta en la lista
        print("Estudiante no encontrado en la lista.")
else: # manejo error por si se ingresa una opcion invalida
    print("Opcion invalida.")