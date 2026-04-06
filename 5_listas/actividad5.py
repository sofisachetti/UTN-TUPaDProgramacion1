# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# ● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# ● Mostrar la lista final actualizada.

estudiantes = ["Ana", "Matias", "Clara", "Nicolas", "Romina", "Juan", "Josefina", "Felipe"]

opcion = input("Elija la acción que desea realizar:\n1- Agregar estudiante\n2- Eliminar estudiante\nOpcion (1 o 2): ")
opcion_validar = opcion.isdigit()
if opcion_validar and opcion == "1":
    nuevo_estudiante = input("\nIngrese el nombre del estudiante: ").capitalize()
    estudiantes.append(nuevo_estudiante)
    print("Estudiante agregado con exito!")
    print("\nLista de estudiantes actualizada: ")
    for e in estudiantes:
        print(e)
elif opcion_validar and opcion == "2":
    estudiante_eliminar = input("Ingrese el nombre del estudiante a eliminar: ").capitalize()
    if estudiante_eliminar in estudiantes:
        estudiantes.remove(estudiante_eliminar)
        print("Estudiante eliminado con exito!")
        print("\nLista de estudiantes actualizada: ")
        for e in estudiantes:
            print(e)
    else:
        print("Estudiante no encontrado en la lista.")
else:
    print("Opcion invalida.")