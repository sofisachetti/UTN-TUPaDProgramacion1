# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)” 
# Contexto 
# Hay 2 días de atención: Lunes y Martes. 
# Cada día tiene cupos fijos: 
    # • Lunes: 4 turnos 
    # • Martes: 3 turnos 
# Reglas 
# 1. Pedir nombre del operador (solo letras). 
# 2. Menú repetitivo hasta salir: 
    # 1. Reservar turno 
    # 2. Cancelar turno (por nombre) 
    # 3. Ver agenda del día 
    # 4. Ver resumen general 
    # 5. Cerrar sistema 
# 3. Reservar: 
    # o Elegir día (1=Lunes, 2=Martes). 
    # o Pedir nombre del paciente (solo letras). 
    # o Verificar que no esté repetido en ese día (comparando con las variables ya cargadas). 
    # o Guardar en el primer espacio libre (ej. lunes1, lunes2…). 
# 4. Cancelar: 
    # o Elegir día. 
    # o Pedir nombre del paciente (solo letras). 
    # o Si existe, cancelar y dejar el espacio vacío (""). 
# 5. Ver agenda del día: 
    # o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío. 
# 6. Resumen general: 
    # o Turnos ocupados y disponibles por día. o Día con más turnos (o empate).


# declaro los turnos que hay por dia
# con lista podria ser turnos_lunes = [turno1, turno2, turno3, turno4]
lunes1 = "" # inicializo con string vacio para despues poder asignarle un paciente despues 
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

turnos_lunes = 4
turnos_martes = 3

print("\nBienvenido al sistema para alta de turnos.\n")

# validacion del operador 
while True:
    operador = input("Ingrese nombre del operador: ")
    if operador.isalpha():
        break # si esta bien corto
    else:
        print("\nError: solo se permiten letras.\n") # si esta mal que vuelva al bucle y empiece de nuevo

# menu
while True:
    print("\nMENÚ PRINCIPAL")
    print("\n1- Reservar turno\n2- Cancelar turno\n3- Ver agenda por día\n4- Ver resumen general\n5- Cerrar sistema\n")

    opcion = input("Ingrese su opcion: ") # guardo la seleccion del usuario en una variable

    if not opcion.isdigit(): # si la opcion no es un numero devuelve error 
        print("Error. Debe ingresar una opción numérica.")
        continue # para que vuelva al menu principal y siga el bucle

    # ----------------OPCION 1--------------
    if opcion == "1":
        print("\nDías disponibles:\n1- Lunes\n2- Martes")
        dia = input("Seleccione el día: ")

        if dia not in ["1", "2"]:  # verificacion para que ingrese solo los dias validos
            print("Error: día inválido.")
            continue

        while True: # aca agrego el nombre del paciente
            nombre = input("Paciente: ")
            if nombre.isalpha():
                break
            else:
                print("Error: el nombre ingresado debe contener solo letras.")

        repetido = False # variable para saber si el turno se repite o no 

        if dia == "1": # opciones para dia lunes
            for i in range(1, turnos_lunes + 1): # for para verificar turnos repetidos 
                if (i == 1 and lunes1 == nombre) or (i == 2 and lunes2 == nombre) or (i == 3 and lunes3 == nombre) or (i == 4 and lunes4 == nombre):
                    repetido = True

            if repetido:
                print("El paciente ya tiene un turno asignado.")
                continue

            # busco turno libre
            asignado = False
            for i in range(1, turnos_lunes + 1):
                if i == 1 and lunes1 == "":
                    lunes1 = nombre
                    asignado = True
                    break
                elif i == 2 and lunes2 == "":
                    lunes2 = nombre
                    asignado = True
                    break
                elif i == 3 and lunes3 == "":
                    lunes3 = nombre
                    asignado = True
                    break
                elif i == 4 and lunes4 == "":
                    lunes4 = nombre
                    asignado = True
                    break

            if not asignado: # si no puedo asignar ninguno doy aviso al usuario
                print("Lunes lleno. Intente sacar turno para el día martes.")
            else:
                print("Turno asignado para el día lunes.")

        else: # opciones para dia martes, sigo la misma logica que con el lunes
            for i in range(1, turnos_martes + 1):
                if (i == 1 and martes1 == nombre) or (i == 2 and martes2 == nombre) or (i == 3 and martes3 == nombre):
                    repetido = True

            if repetido:
                print("El paciente ya tiene un turno asignado.")
                continue

            asignado = False
            for i in range(1, turnos_martes + 1):
                if i == 1 and martes1 == "":
                    martes1 = nombre
                    asignado = True
                    break
                elif i == 2 and martes2 == "":
                    martes2 = nombre
                    asignado = True
                    break
                elif i == 3 and martes3 == "":
                    martes3 = nombre
                    asignado = True
                    break

            if not asignado:
                print("Martes lleno. Intente sacar turno para el dia lunes")
            else:
                print("Turno asignado para el día martes.")

# ----------------OPCION 2--------------
    elif opcion == "2":
        print("\nCancelar turno\n")
        dia = input("Seleccione el día (1 = Lunes, 2 = Martes): ")

        if dia not in ["1", "2"]:
            print("Error: día inválido.")
            continue

        nombre = input("Nombre del paciente: ") # tengo que buscar por nombre

        if not nombre.isalpha():
            print("Error: el nombre ingresado debe contener solo letras.")
            continue

        encontrado = False

        if dia == "1": # si el dia ingresado es lunes, busco en los turnos de ese dia
            if lunes1 == nombre:
                lunes1 = ""
                encontrado = True
            elif lunes2 == nombre:
                lunes2 = ""
                encontrado = True
            elif lunes3 == nombre:
                lunes3 = ""
                encontrado = True
            elif lunes4 == nombre:
                lunes4 = ""
                encontrado = True

        else: # sino busco en los turnos del martes
            if martes1 == nombre:
                martes1 = ""
                encontrado = True
            elif martes2 == nombre:
                martes2 = ""
                encontrado = True
            elif martes3 == nombre:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado con exito.")
        else:
            print("Paciente no encontrado.")

# ----------------OPCION 3--------------
    elif opcion == "3":
        print("\nAgenda por día\n")
        dia = input("Ingrese el dia que quiera consultar (1 = Lunes, 2 = Martes): ")

        if dia == "1":
            print("\nAgenda Lunes:")
            for i in range(1, 5):
                if i == 1:
                    valor = lunes1
                elif i == 2:
                    valor = lunes2
                elif i == 3:
                    valor = lunes3
                else:
                    valor = lunes4

                print("Turno", i, ":", valor if valor != "" else "(libre)")

        elif dia == "2":
            print("\nAgenda Martes:")
            for i in range(1, 4):
                if i == 1:
                    valor = martes1
                elif i == 2:
                    valor = martes2
                else:
                    valor = martes3

                print("Turno", i, ":", valor if valor != "" else "(libre)")

# ----------------OPCION 4--------------
    elif opcion == "4":
        ocupados_lunes = 0
        ocupados_martes = 0

        for i in range(1, turnos_lunes + 1):
            if (i == 1 and lunes1 != "") or (i == 2 and lunes2 != "") or (i == 3 and lunes3 != "") or (i == 4 and lunes4 != ""):
                ocupados_lunes += 1

        for i in range(1, turnos_martes + 1):
            if (i == 1 and martes1 != "") or (i == 2 and martes2 != "") or (i == 3 and martes3 != ""):
                ocupados_martes += 1

        print("\nResumen general:\n")
        print("- Lunes:", ocupados_lunes, "ocupados")
        print("- Martes:", ocupados_martes, "ocupados")

# ----------------OPCION 5--------------
    elif opcion == "5":
        print("Cerrando sistema...")
        break