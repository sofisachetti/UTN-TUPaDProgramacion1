# Sistema de control de inventario - 2° Parcial Programación I
# Tecnicatura Universitaria en Programación a Distancia - UTN
# Alumna: Sofía Sachetti


# Función menu(): 
# solamente imprime las opciones que hay disponibles.
def menu():
    print("\n------ SISTEMA DE CONTROL DE INVENTARIO ------")
    print("\nMenú de opciones: ")
    print("1- Carga incial de herramientas")
    print("2- Ver inventario")
    print("3- Consultar stock")
    print("4- Reporte de agotados")
    print("5- Alta d enuevo producto")
    print("6- Venta / Ingreso")
    print("7- Salir")

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
                    raise ValueError("El nombre debe ser una cadena de caracteres.")
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
                    raise ValueError("El stock inicial no puede ser negativo.")
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
        print(" --------  INVENTARIO COMPLETO  -------- ")   # Recorro el inventario con un bucle for 
        for i in range(len(inventario)):
            print(f"{i} - {inventario[i]['herramienta']} - {inventario[i]['cantidad']}")
        print("-" * 40)
        print(f"Total de productos: {len(inventario)}")

inventario = [{"herramienta": "martillo", "cantidad": 15}, {"herramienta": "pinza", "cantidad": 10},{"herramienta": "clavos", "cantidad": 1500}]

mostrar_inventario(inventario)