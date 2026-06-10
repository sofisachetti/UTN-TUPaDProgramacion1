# Sistema de control de inventario - 2° Parcial Programación I
# Tecnicatura Universitaria en Programación a Distancia - UTN
# Alumna: Sofía Sachetti


# Funcion auxiliar nombre_normalizado():
# Recibe como parámetro el nombre de una herramienta y lo pasa a un formato normalizado
# Su funcion es que todos los nombres queden almaccenados de la misma forma
def nombre_normalizado(nombre):
    nombre = nombre.strip().lower()
    return nombre


# Funcion auxiliar herramienta_existe(): 
# Acá se verifica que la herramienta no esté actualmente dentro del inventario
# Se va a usar cada vez que se consulte por una herramienta o se quiera ingresar una nueva.
def herramienta_existe(inventario, nombre):
    nombre = nombre_normalizado(nombre)
    for item in inventario:
        if item["herramienta"].strip().lower() == nombre:
            return True # Si la herramienta ya existe retorna True, sino False
    return False


# Funcion auxiliar verificar_inventario(): para corroborar si el inventario tiene herramientas cargadas o está vacio.
def inventario_vacio(inventario):
    if len(inventario) == 0:
        print("\nNo hay herramientas cargadas en el inventario.")
        print("Para hacer la carga incial de herramientas seleccione la opción 1.")
        return True

# ------------------------------------------------------------------------------------------------------------
# Función cargar_herramientas() para la opción 1:
# Sólo se va a ejecutar si el inventario está vacio, es la carga inicial del stock.
# Recibe como parámetro el inventario. Si está vacío, hace la carga incial de herramientas.
# Si ya tiene herramientas cargadas, avisa que se debe utilizar la opción 5.
def cargar_herramientas(inventario):
    
    # Acá se hace la verificación incial para saber si el inventario está vacío.
    # Si el inventario ya tiene herramientas cargadas, avisa que se debe usar la opción 5.
    if len(inventario) != 0: 
        print("\nEl inventario ya tiene herramientas cargadas.")
        print("Para agregar nuevos productos o actualizar stock, elija la opción 5.")
        return inventario

    # Primer bucle: en este se controla la cantidad de herramientas a cargar.
    # Se le pide al usuario un número y se verifica: 
    # - que sea num positivo   
    # - que sea num entero, con manejo de error si eso no pasa
    cantidad = 0
    while cantidad <= 0:
        try:
            cantidad = int(input("\nIngrese la cantidad de herramientas a cargar: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser un número entero mayor que cero. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

    # Segundo bucle para manejar la carga de herramientas. Acá el controlador es el contador de herramientas que se fueron cargando.
    cargadas = 0
    while cargadas < cantidad:
        # Bucle anidado para maejar el flujo del ingreso dle nombre. 
        # Si el usaurio no cumple con los requisitos, lo debe volver a intentar hasta que esté correcto.
        nombre_valido = False
        while not nombre_valido:
            try:
                nombre = input(f"\nIngrese el nombre - Herramienta {cargadas + 1}: ")
                if nombre.strip() == "": # Verifica que no sea nombre vacio
                    raise ValueError("El nombre no puede estar vacío. Intente nuevamente.")
                if not nombre.isalpha():  # Verifica que sea un string de letras
                    raise ValueError("El nombre debe ser una cadena de caracteres. Intente nuevamente.")
                if herramienta_existe(inventario, nombre): # Verifica si la herramienta existe en el inventario
                    raise ValueError(f"Ya existe una herramienta con ese nombre. Intente nuevamente.")
                nombre_valido = True
                nombre = nombre_normalizado(nombre)
            except ValueError as e: # Maneja cualquier otro error
                print(f"Error: {e}")

        # Segundo bucle anidado que maneja el ingreso de la cantidad de cada herramienta,
        # Si el usuario lo hace de forma incorrecta, se sigue insistiendo hasta que lo haga de forma correcta
        stock_valido = False
        while not stock_valido:
            try:
                stock = int(input(f"Ingrese el stock inicial - Herramienta {cargadas + 1}: "))
                if stock <= 0: # Valido que el num ingresado sea positivo
                    raise ValueError("El stock inicial no puede ser negativo o cero. intente nuevamente.")
                stock_valido = True
            except ValueError as e:
                print(f"Error: {e}")

        # Agregar al inventario, manteniendo el formato de diccionario
        inventario.append({"herramienta": nombre, "cantidad": stock})
        print(f"- Herramienta '{nombre}' agregada al stock con {stock} unidades.")
        cargadas += 1

    print(f"\nCarga completada. {cantidad} herramientas registradas.")
    return inventario


# ---------------------------------------------------------------------------------------------------------------
# Funcion mostrar_inventario() para la opción 2.
# Recibe el inventario como parámetro y lo imprime por consola con formato
def mostrar_inventario(inventario):
    if inventario_vacio(inventario): # Verifica si el inventario está vacio
        return
    else:
        print("\n --------  INVENTARIO COMPLETO  -------- ")   # Recorro el inventario con un bucle for 
        for i in range(len(inventario)):
            print(f"{i + 1} - {inventario[i]['herramienta']} - {inventario[i]['cantidad']}")
        print("-" * 40)
        print(f"Total de productos: {len(inventario)}")


# ---------------------------------------------------------------------------------------------------------------
# Funcion consultar_stock() para la opción 3
# Busca una herramienta por nombre y muestra su stock, recibe como parametro el inventario
def consultar_stock(inventario):
    if inventario_vacio(inventario):  # Verifico que el inventario no este vacio
        return
    else:
        nombre = input("\nIngrese el nombre de la herramienta a consultar: ")
        nombre = nombre_normalizado(nombre) # normalizo el nombre qu eingresa el usuario para que coincida con el formato almacenado

        for i in inventario:  # Recorro con bucle for, si el nombre almacenado coincide con el ingresado lo imprimo en consola
            if i["herramienta"] == nombre:  
                print(f"\n'{i['herramienta']}' - Stock disponible: {i['cantidad']} unidades.")
                return
        # Si la herramienta no se encuentra, se da aviso
        print(f"\nLa herramienta '{nombre}' no se encuentra en el catálogo.")


# ---------------------------------------------------------------------------------------------------------------
# Funcion reporte_agotados para la opcion 4
# Recibe como parametro el inventario y devuelve las herramientas que tengan como cantidad 0.
def reporte_agotados(inventario):
    if inventario_vacio(inventario):  # Verifico si el inventario esta vacio
        return
    else:
        agotados = []   # inicializo variable para almacenar los productos agotados si hay
        for item in inventario:
            if item["cantidad"] == 0: # recorro con bucle for, si en "cantidad" alguno tiene 0, lo almaceno en el array de agotados
                agotados.append(item)

        if len(agotados) == 0:   # Si el array de agotados está en 0, significa que no hay herramientas agotadas
            print("\nNo hay productos agotados.")
            return

        print("\n------- PRODUCTOS AGOTADOS -------")  # Sino, imprimo el reporte mostrando las herramientas agotadas
        for item in agotados:
            print(f"- {item['herramienta']}")
        print(f"\nTotal agotados: {len(agotados)}")


# ---------------------------------------------------------------------------------------------------------------
# Funcion alta_producto() para opcion 5
# Agrega una herramienta nueva al inventario
# Si hay algún error de validación, informa y vuelve al menú
# Retorna el inventario actualizado
def alta_producto(inventario):
    try:
        nombre = input("\nNombre de la nueva herramienta: ")
        nombre = nombre_normalizado(nombre) # normalizo el nombre para que ingrese de la misma forma que esta almacenado
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")
        if herramienta_existe(inventario, nombre):
            raise ValueError(f"Ya existe una herramienta llamada '{nombre}' en el stock.")

        # Validaciones del stock
        stock = int(input("Stock inicial: "))
        if stock <= 0:
            raise ValueError("El stock inicial no puede ser negativo o cero.")

        inventario.append({"herramienta": nombre.strip(), "cantidad": stock})
        print(f"\nHerrmienta '{nombre.strip()}' agregada con {stock} unidades.")
    # Si hay error, vuelve al menu princiapl
    except ValueError as e:
        print(f"\nError: {e}")
        print("Volviendo al menú principal sin agregar el producto.")

    return inventario


# ---------------------------------------------------------------------------------------------------------------
# Funcion actualizar_stock() para la opcion 6
# Recibe de parametro el inventario. Registra una venta o actualiza el stock actual
def actualizar_stock(inventario):
    nombre = input("\nIngrese el nombre de la herramienta: ")  # Pido nombre de herramienta y normalizo la entrada
    nombre = nombre_normalizado(nombre)

    # Busco la herramienta en el inventario
    indice = -1
    for i in range(len(inventario)):
        if inventario[i]["herramienta"] == nombre:
            indice = i
            break
    # Si no encuentra la herramienta, aviso al usuario
    if indice == -1:
        print(f"\nLa herramienta '{nombre}' no se encuentra en el stock.")
        return inventario

    herramienta = inventario[indice]  # Muestro la info actual de la herramienta y le pregunto al usuario que accion hacer
    print(f"\nHerramienta: {herramienta['herramienta']}")
    print(f"Stock actual: {herramienta['cantidad']} unidades")
    print("\n¿Qué operación desea realizar?")
    print("1. Venta")
    print("2. Ingreso")

    try:
        opcion = int(input("\nSeleccione 1 o 2: "))
        if opcion not in [1, 2]: # Si la opcion del usuario no es 1 o 2, muestro error y vuelvo al menu
            raise ValueError("Opción inválida. Debe ser 1 (Venta) o 2 (Ingreso). Volviendo al menú principal.")

        cantidad = int(input("Cantidad: "))  # Le pido que ingrese la cantidad a vender o actualizar
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero mayor que cero.")

        if opcion == 1:
            # Venta: verifico que el stock sea correcto para hacer la venta
            if cantidad > herramienta["cantidad"]:
                raise ValueError(f"Stock insuficiente. Disponible: {herramienta['cantidad']} unidades.")
            inventario[indice]["cantidad"] -= cantidad
            print(f"\nVenta registrada. Stock actualizado: {inventario[indice]['cantidad']} unidades.")

        else:
            # Ingreso: sumo la cantidad ingresada a la cantidad almacenada
            inventario[indice]["cantidad"] += cantidad
            print(f"\nIngreso registrado. Stock actualizado: {inventario[indice]['cantidad']} unidades.")

    except ValueError as e:
        print(f"\nError: {e}")

    return inventario


# ---------------------------------------------------------------------------------------------------------------
# Funcion menu()
# Maneja la logica principal del sistema
# Dentro de ella se define el inventario y con le bucle while se maneja el flujo
def menu():
    inventario = []
    opcion = 0

    while True:
        
        print("\n------ SISTEMA DE CONTROL DE INVENTARIO ------")
        print("\nMenú de opciones: ")
        print("1- Carga incial de herramientas")
        print("2- Ver inventario")
        print("3- Consultar stock")
        print("4- Reporte de agotados")
        print("5- Alta de nuevo producto")
        print("6- Venta / Ingreso")
        print("7- Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))

            if opcion == 1:
                print("\n------- CARGA INICIAL DE STOCK -------")
                inventario = cargar_herramientas(inventario)
            elif opcion == 2:
                print("\n------- VER INVENTARIO -------")
                mostrar_inventario(inventario)
            elif opcion == 3:
                print("\n------- CONSULTA DE STOCK -------")
                consultar_stock(inventario)
            elif opcion == 4:
                print("\n------- REPORTE DE AGOTADOS -------")
                reporte_agotados(inventario)
            elif opcion == 5:
                print("\n------- ALTA NUEVO PRODUCTO -------")
                inventario = alta_producto(inventario)
            elif opcion == 6:
                print("\n------- VENTA / INGRESO -------")
                inventario = actualizar_stock(inventario)
            elif opcion == 7:
                print("\nCerrando el sistema... ¡Hasta pronto!\n")
                break
            else:
                raise ValueError("La opción debe estar entre 1 y 7.")

        except ValueError as e:
            print(f"\nOpción inválida: {e}")
            opcion = 0


menu()
