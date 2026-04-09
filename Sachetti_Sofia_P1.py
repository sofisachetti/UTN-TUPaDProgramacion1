# El programa debe presentar un menú interactivo persistente con las siguientes opciones: MENU - LISTO

# 1. Carga Inicial de Herramientas: Registrar los nombres de las herramientas que se
# pondrán a la venta. Se debe preguntar al usuario la cantidad de herramientas a cargar
# y se debe usar una estructura pertinente. En caso de nombre vacío o duplicado se
# debe seguir pidiendo hasta que sea correcto respetando la cantidad de herramientas
# que el usuario indicó antes de la carga.  LISTO

# 2. Carga de Existencias: Ingresar la cantidad de unidades para cada herramienta
# registrada previamente, respetando el orden de ingreso. Cuando el usuario ingresa
# existencias, el sistema debe mostrar por pantalla el nombre de la herramienta.

# 3. Visualización de Inventario: Mostrar el listado completo de herramientas junto a su
# stock actual.

# 4. Consulta de Stock (existencias): Buscar una herramienta por su nombre y mostrar
# cuántas unidades hay disponibles.

# 5. Reporte de Agotados: Listar únicamente aquellos productos cuyo stock sea igual a
# cero.

# 6. Alta de Nuevo Producto: Permitir agregar solo una nueva herramienta al final de las
# listas con su stock inicial. En caso de nombre vacío, nombre duplicado o valor de
# existencia negativo se debe volver al menú principal mostrando por pantalla el motivo

# 7. Actualización de Stock (Venta/Ingreso):
# o Venta: Disminuir el stock tras validar que hay unidades suficientes.
# o Ingreso: Aumentar el stock por reposición de mercadería.

# 8. Salir: Finalizar la ejecución del sistema. FINALIZAR EJECUCION - LISTO

# Inicialización de listas, ambas tienen que estar relacionadas entre sí.
herramientas = []
existencias = []

# Variable para controlar el seguimiento del menu
control_menu = True

print("----- SISTEMA PARA CONTROL DE STOCK -----")

# Bucle para el control general del menu
while control_menu:
    print("\nMENÚ PRINCIPAL")
    print("1- Carga de herramientas")
    print("2- Carga de existencias")
    print("3- Ver inventario")
    print("4- Consulta de Stock")
    print("5- Reporte de agotados")
    print("6- Alta Nuevo Producto")
    print("7- Actualizar Stock")
    print("8- Salir")
    opcion = input("Ingrese su opción: ")
    
    # Validación del input: si la opcion no es un numero devuelve un mensaje de error 
    if not opcion.isdigit(): 
        print("\nError. Debe ingresar una opción numérica.")
        continue # Para que vuelva al menu principal y siga el bucle
    
    # Manejo de las opciones del menu con condicional
    if opcion == "1":
        print("--- CARGA DE HERRAMIENTAS ---")
        
        # Pido la cantidad de herramientas e inicializo un contador de las mismas en 0 para el bucle
        cantidad_herramientas = input("Ingrese la cantidad de herramientas para cargar en el sistema: ")
        contador = 0
        
        # Verifico que la cantidad de herramientas ingresada sea en formato numerico
        if not cantidad_herramientas.isdigit():
            print("Error: debe ingresar la cantidad de herramientas en forma numérica.")
        else:
            cantidad_herramientas = int(cantidad_herramientas) # Transformo el string en un numero entero
        
        # Mientras el contador sea menor a la cantidad de herramientas a ingresar
        while contador < cantidad_herramientas:
            nombre_herramienta = input("Ingrese el nombre de la herramienta: ").capitalize()
            
            # Valido que el nombre ingresado no sea un string vacio
            if not nombre_herramienta.isalpha():
                print("Error. No puede ingresar un nobre vacio.")
            elif nombre_herramienta in herramientas:
                print("La herramienta ingresada ya se encuentra dentro del inventario.")
            else:
                herramientas.append(nombre_herramienta)
                contador += 1
        print(herramientas)

    elif opcion == "2":
        print("--- CARGA DE EXISTENCIAS ---")
    elif opcion == "3":
        print("--- VER INVENTARIO ---")
    elif opcion == "4":
        print("--- CONSULTA DE STOCK ---")
    elif opcion == "5":
        print("--- REPORTE DE AGOTADOS ---")
    elif opcion == "6":
        print("--- ALTA DE NUEVO PRODUCTO ---")
    elif opcion == "7":
        print("--- ACTUALIZAR STOCK ---")
    elif opcion == "8":
        print("--- SALIR ---")
        control_menu = False