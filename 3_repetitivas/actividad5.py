# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

# 1. Descripción del Escenario
# Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un
# usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El
# objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo.
# Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de
# control (if/elif/else), ciclos (while y for) y validación de datos estricta.

# 2. Requerimientos Técnicos
# A. Tipos de Datos
# Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:
    # •  String: Para el nombre del jugador.
    # •  Int: Para los Puntos de Vida (HP) y cantidad de pociones.
    # •  Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5)
    # •  Boolean: Para controlar si el juego sigue activo o quién tiene el turno.
# B. Reglas de Validación (¡Importante!)
    # •  No está permitido usar bloques try / except.
    # •  Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.
    # •  Para validar números, debes usar el método .isdigit() dentro de un ciclo while.

# 3. Flujo del Programa
# Paso 1: Configuración del Personaje
# El programa inicia pidiendo el nombre del Gladiador.
    # •  Validación: El nombre solo puede contener letras. Si el usuario ingresa números, símbolos o lo deja vacío, 
    # el programa debe decir "Error: Solo se permiten letras" y volver a preguntar hasta que sea válido.
# Paso 2: Inicialización de Estadísticas
# El programa debe definir las variables iniciales (sin preguntar al usuario):
    # •  Vida del Gladiador: 100 (int)
    # •  Vida del Enemigo: 100 (int)
    # •  Pociones de Vida: 3 (int)
    # •  Daño base "Ataque Pesado": 15 (int)
    # •  Daño base del enemigo: 12 (int)
    # •  Turno Gladiador : True (booleano)
# Paso 3: El Ciclo de Combate
# El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 puntos de vida.
# Turno del Jugador:
# Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3 opciones:
# 1. Ataque Pesado
# 2. Ráfaga Veloz (Requiere uso de for)
# 3. Curar
    # • Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo ingresado sea un número (.isdigit()).
# 2. Verificar que el número sea 1, 2 o 3.
    # o Si falla alguna validación, mostrar mensaje de error y volver a pedir.

# Lógica de las Acciones:
# Acción A: Ataque Pesado (Opción 1)
# •  Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador
# realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).
# •  Resta el daño a la vida del enemigo.
# •  Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"
# Acción B: Ráfaga Veloz (Opción 2)
# •  Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.
# •  El bucle debe repetirse 3 veces (usando range).
# •  Dentro del bucle, en cada repetición: 
#       1. Resta 5 puntos de daño a la vida del enemigo.
#       2. Muestra el mensaje: " > Golpe conectado por 5 de daño".
# Acción C: Curar (Opción 3) 
# • • Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.
# • • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el
# enemigo ataca igual).
# Turno del Enemigo:
# Justo después de tu acción, el enemigo ataca automáticamente.
# • • Resta el daño base del enemigo (12) a tu vida.
# • • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"
# Paso 4: Fin del Juego
# Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:
# • • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."
# • • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate."



# defino las variables inciiales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_jugador = True      

# nombre del jugador y verificacion
while True:
    nombre = input("Ingrese el nombre del Gladiador: ")
    if nombre.isalpha():
        break # si el nombre cumple con la condicion entonces sale del bucle
    else:
        print("Error: Solo se permiten letras.\n")


print(f"\n¡Bienvenido al juego, {nombre}!\n")

# bucle para el combate
while vida_jugador > 0 and vida_enemigo > 0: # mientras ambos tengan puntos de vida

    # si es el turno del jugador se ejecutan las opciones
    if turno_jugador:
        # imprime la info 
        print("\n___ ESTADO ___")
        print(f"Tu vida: {vida_jugador}")
        print(f"Vida enemigo: {vida_enemigo}")
        print(f"Pociones disponibles: {pociones}")

        print("\n1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        # valido la opcion que elija
        while True:
            opcion = input("Elegí una opción: ")
            if opcion.isdigit() and opcion in ["1", "2", "3"]:
                break
            else:
                print("Error: opción inválida.")

        # primera opcion de ataque
        if opcion == "1":
            if vida_enemigo < 20: # corroboro la vida del enemigo para hacer daño final
                danio_final = danio_pesado * 1.5  # float
                print("¡Golpe crítico!")
            else:
                danio_final = danio_pesado

            vida_enemigo -= danio_final # resto puntos del enemigo
            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

        # segunda opcion de ataque
        elif opcion == "2":
            print("Realizando ráfaga veloz...")
            for i in range(3):
                vida_enemigo -= 5
                print(" -> Golpe conectado por 5 de daño")

        # tercera opcion para curar
        elif opcion == "3":
            if pociones > 0: # si hay pociones disponibles:
                vida_jugador += 30 # aumento vida
                pociones -= 1 # resto del inventario de pociones

                if vida_jugador > 100: # verifico que el puntaje de vida no supere los 100 puntos
                    vida_jugador = 100

                print("Ahora tiene 30 puntos mas de vida.")
            else:
                print("¡No quedan mas pociones!")

        # cambia turno y pasa a jugar el enemigo
        turno_jugador = False
    # cambio al turno del enemigo
    else:
        if vida_enemigo > 0: # si tiene puntos de vida disponibles
            vida_jugador -= danio_enemigo # le resto a la vida dle jugador los puntos de ataque
            print(f"\n¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

        turno_jugador = True # pasa de nuevo al turno del jugador

# termino el juego mostrando los resultados
print("\n___ RESULTADO ___")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")