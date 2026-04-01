# Ejercicio 2 — “Acceso al Campus y Menú Seguro”
# Objetivo: Login con intentos + menú de acciones con validación estricta.
# Requisitos
# 1. Definir credenciales fijas en el código:
#   o usuario correcto: "alumno"
#   o clave correcta: "python123"
# 2. Permitir máximo 3 intentos para ingresar usuario y clave.
# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#   1. Ver estado de inscripción (mostrar “Inscripto”)
#   2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
#   3. Mostrar mensaje motivacional (1 frase)
#   4. Salir
# 5. Validación del menú:
#   o Debe ser número (.isdigit())
#   o Debe estar entre 1 y 4
# Cambio de clave
# • La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, rechazar.


# primero hago definicion de credenciales
usuario = "alumno"
clave = "python123"
login = False # bandera 

print("\n¡Bienvenida/o al Campus Virtual!\n")

# Intentos de login
for i in range(3): # empieza del 0 al 2
    usuario_ingresado = input("Igrese su usuario: ").lower() # el input que ingresa lo guardo en lower case para que coincida con el que tengo ingresado
    clave_ingresada = input("Ingrese su clave: ").lower()

    if usuario_ingresado == usuario and clave_ingresada == clave: # valido los datos ingresados con los almacenados
        login: True
        print("\nInicio de sesión exitoso.\n")
        
        # menu
        while True:
            print("\nMenú de opciones:\n1- Ver estado de inscripción\n2- Cambiar clave\n3- Ver frase motivacional del día\n4- Salir")
            opcion = input("\nIngresa el número de opción: ") # almaceno la opcion que ingresa el usuario
            
            # validaciones de las opciones
            if opcion.isdigit():
                if opcion == "1":
                    print("\nSu estado es: Inscripto\n")
                elif opcion == "2":
                    clave_actual = input("\nIngrese su clave actual: ") # confirmo la clave actual
                    if clave == clave_actual: # si coincide paso a hacer el cambio
                        while True:
                            nueva_clave = input("\nIngrese su nueva clave (minimo 6 caracteres): ").lower()
                            conf_clave = input("Confirme su nueva clave: ").lower()
                            if len(nueva_clave) >= 6 and nueva_clave == conf_clave: # validaciones
                                clave = nueva_clave # guardo la nueva clave
                                print("\nClave cambiada con éxito.\n")
                                break
                            else:
                                print("\nLas claves ingresadas no coinciden o no cumple con la longitud especificada.\n")
                    else:
                        print("\nClave actual incorrecta.")
                elif opcion == "3":
                    print("\nFrase motivacional del día: \n")
                    print('\n"Si puedes soñarlo, puedes hacerlo."\n')
                elif opcion == "4":
                    print("\nSaliendo del sistema. ¡Hasta la próxima!\n")
                    break
                else:
                    print("\nLa opción ingresada es invalida. Aseguráte que sea un numero entre 1 y 4.\n") # error si el usuario ingresa un numero fuera del rango
            else: 
                print("\nOcurrio un error. Asegurate que la opción que ingreses sea numérica.\n") # error si el usuario ingresa un caracter no numerico
        break # para salir del for
    
    # si los intentos son incorrectos
    else:
        if i < 2: # si los intentos son menos de 2 deja intentar de nuevo
            print("\nCredenciales incorrectas. Intente nuevamente.\n")
        elif i == 2: # sino la cuenta se bloquea y cerramos el bucle
            print("\nHa excedido la cantidad de intentos. Cuenta bloqueada.")   
