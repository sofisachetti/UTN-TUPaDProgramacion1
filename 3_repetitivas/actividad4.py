# Ejercicio 4 — “Escape Room: La Bóveda”
# Historia
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
# Variables iniciales (NO se piden por teclado)
    # • energia = 100
    # • tiempo = 12
    # • cerraduras_abiertas = 0
    # • alarma = False
    # • codigo_parcial = ""
# Validaciones obligatorias
    # • No usar try/except.
    # • Pedir nombre del agente y validar con .isalpha() en un while.
    # • Validar opciones del menú y cualquier número pedido con .isdigit() en un while.
    # • El juego debe funcionar con estructuras secuenciales, condicionales y repetitivas (puede usar funciones propias del 
    # lenguaje como .lower(), len(), formateo, etc.).
# Regla anti-spam (muy importante)
# Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al iniciar:
# Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
    # • se cobra el costo normal (-20 energía, -2 tiempo),
    # • NO abre cerradura, y
    # • se activa la alarma automáticamente (alarma = True) porque “la cerradura se trabó”.
# Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.
# Menú de acciones (se repite mientras el juego siga)
# El juego continúa mientras:
    # • energia > 0, tiempo > 0, cerraduras_abiertas < 3
    # • y no esté bloqueado por alarma.
# En cada turno mostrar el estado y el siguiente menú:
# 1. Forzar cerradura (costo: -20 energía, -2 tiempo)
    # o Si la energía está por debajo de 40, hay “riesgo de alarma”:
    # ▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True.
    # o Si no hay alarma, abre 1 cerradura.
    # o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y no abre.
# 2. Hackear panel (costo: -10 energía, -3 tiempo)
    # o Debe usar un for de 4 pasos mostrando progreso.
    # o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”).
    # o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si todavía faltan.
# 3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)
# Regla de bloqueo por alarma
    # • Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema se bloquea y se pierde.
# Condiciones de fin
    # • Si cerraduras_abiertas == 3 → VICTORIA
    # • Si energia <= 0 o tiempo <= 0 → DERROTA
    # • Si se bloquea por alarma → DERROTA (bloqueo)



# declaracion de variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

cont_forzar = 0  # conteo para la regla anti spam

# verificacion de nombre
while True:
    agente = input("Ingrese nombre del agente: ")
    if agente.isalpha():
        break
    else:
        print("Error: el nombre solo puede contener letras.\n")

print(f"\nBienvenido agente {agente}. La misión de hoy es abrir la bóveda.\n")

# logica del juego, mientras tenga energia y tiempo y las cerraduras no esten abiertas se muestra en bucle el menu
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # condicion para bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\nSistema bloqueado por alarma. Misión fallida.")
        break # se pierde el juego asi que corto el bucle

    # imprimo los estados
    print("\n___ ESTADO ___")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVA' if alarma else 'INACTIVA'}") # si alarma esta en True imprime que esta activa

    # menu de opciones
    print("\n1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    # valido las opciones con isdigit()
    while True:
        opcion = input("Elegí una opción: ")
        if opcion.isdigit() and opcion in ["1", "2", "3"]:
            break
        else:
            print("Opción inválida.")

    # logica para opcion 1 - forzar
    if opcion == "1":
        energia -= 20 # resta energia/tiempo
        tiempo -= 2
        cont_forzar += 1 # suma al contador

        # validacion anti spam
        if cont_forzar == 3:
            print("\nForzaste demasiado seguido y la cerradura se trabó.")
            alarma = True # pasa a sonar la alarma
            cont_forzar = 0 # el contador vuelve a 0
            continue

        # si energía < 40
        if energia < 40:
            print("\nEnergía baja, riesgo de alarma.")
            while True: # logica para la seleccion del numero
                riesgo = input("Elegí un número (1-3): ")
                if riesgo.isdigit() and riesgo in ["1", "2", "3"]:
                    break
                else:
                    print("Número inválido.")

            if riesgo == "3": # si selecciona el 3 se activa la alarma
                print("Se activó la alarma.")
                alarma = True
                continue

        # si no suena la alarma, abre la cerradura
        if not alarma:
            cerraduras_abiertas += 1
            print("Cerradura abierta.")

    # opcion para hackear
    elif opcion == "2":
        energia -= 10 # baja energia y tiempo
        tiempo -= 3
        cont_forzar = 0  # corta la racha de forzado

        print("\nHackeando panel...")

        for i in range(4): 
            codigo_parcial += "A"
            print(f"Progreso: {i+1}/4 | Código: {codigo_parcial}") # imprime progreso del codigo con cada vuelat

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3: # si se llega a la longitud y quedan cerraduras sin abrir
            cerraduras_abiertas += 1 # agrego una mas a las cerraduras abiertas
            print("Cerradura abierta automáticamente por hackeo.")

    # descanso
    elif opcion == "3":
        energia += 15 # modifico la enrgia
        if energia > 100: # condicional para que no supere los 100 puntos
            energia = 100

        tiempo -= 1 # modifico el tiempo
        cont_forzar = 0  # corta la racha del forzado

        if alarma: # si suena la alarma resta energia
            energia -= 10
            print("La alarma consume energia extra.")

        print("Descansaste.")

# imprimo resultados finales 
if cerraduras_abiertas == 3:
    print("\n¡Mision completa! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("\nDERROTA: Te quedaste sin recursos.")
elif alarma and tiempo <= 3:
    print("\nDERROTA: Sistema bloqueado por alarma.")