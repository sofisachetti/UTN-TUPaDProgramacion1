# Sofia Sachetti
# Programación I - 1er Parcial
# Tecnicatura Universitaria en Programación - UTN


# Inicialización de listas vacías, ambas tienen que estar relacionadas entre sí
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
    
    # Validación del input: si la opcion no es un número devuelve un mensaje de error 
    if not opcion.isdigit(): 
        print("\nError. Debe ingresar una opción numérica.")
        continue # Para que vuelva al menu principal y siga el bucle
    
    # Manejo de las opciones del menu con condicional if - elif
    if opcion == "1":
        print("\n--- CARGA DE HERRAMIENTAS ---")
        
        # Pido la cantidad de herramientas e inicializo un contador de las mismas en 0 para el bucle
        cantidad_herramientas = input("Ingrese la cantidad de herramientas para cargar en el sistema: ")
        contador = 0
        
        # Verifico que la cantidad de herramientas ingresada sea en formato numerico
        if not cantidad_herramientas.isdigit():
            print("Error: debe ingresar la cantidad de herramientas en forma numérica.")
            continue
        else:
            cantidad_herramientas = int(cantidad_herramientas) # Transformo el string en un numero entero
        
        # Mientras el contador sea menor a la cantidad de herramientas a ingresar
        while contador < cantidad_herramientas:
            nombre_herramienta = input(f"Ingrese el nombre de la herramienta {contador + 1}: ").capitalize()
            
            # Valido que el nombre ingresado no sea un string vacio
            if not nombre_herramienta.isalpha():
                print("Error. No puede ingresar un nobre vacio o numérico.")
            elif nombre_herramienta in herramientas: # Valido que la herramienta no esté repetida
                print("La herramienta ingresada ya se encuentra dentro del inventario.")
            else: # Si cumple con las condiciones, la agrego a la lista de herramientas y sumo el contador
                herramientas.append(nombre_herramienta)
                contador += 1
        
        for i in herramientas:
            print(i)
    
    elif opcion == "2":
        print("\n--- CARGA DE EXISTENCIAS ---")
        
        # Primero verifico que la lista de herramientas no esté vacía
        if not herramientas: 
            print("El listado de herramientas está vacío. \nIngrese a la opción 1 para carga de herramientas.")
        else:
            existencias.clear() # Limpio la lista de existencias, me va a pedir cargar nuevamente una por una
            
            for i in range(0, len(herramientas)): # Recorro la lista de herramientas 
                while True: 
                    print(f"Agregar existencia para {herramientas[i]}.") # Muestro la herramienta
                    cantidad = input("Cantidad: ") # Pido al usuario la cantidad
                
                    if not cantidad.isdigit() or int(cantidad) < 0: # Si la cantidad no es un numero o es menor a o devuelve error
                        print("Número inválido. Intente nuevamente.") 
                        continue
                    else: 
                        cantidad = int(cantidad) # Pasamos la cantidad a numero entero
                        existencias.append(cantidad) # La agregamos a la lista de existencias
                        break # Terminamos el bucle para que pase al proximo elemento de la lista
        
        # Muestro en pantalla la lista final de herramientas
        for i in range(0, len(herramientas)):
            print(f"{herramientas[i]} - {existencias[i]}")
        
    elif opcion == "3":
        print("\n--- VER INVENTARIO ---")
        
        # Primero verifico que la lista de herramientas no esté vacía
        if not herramientas: 
            print("El listado de herramientas está vacío. \nIngrese a la opción 1 para carga de herramientas.")
        
        # Imprimo las herramientas y su stock correspondiente
        for i in range(0, len(herramientas)):
            print(f"{i + 1}- {herramientas[i]} - Stock: {existencias[i]}")
    
    elif opcion == "4":
        print("\n--- CONSULTA DE STOCK ---")
        
        if not herramientas: # Primero verifico si el listado de herramientas está vacio
            print("El listado de herramientas está vacío. \nIngrese a la opción 1 para carga de herramientas.")
            continue

        nombre_buscado = input("Ingrese la herramienta a consultar: ").capitalize() # Pido nombre de la herramienta a buscar
        encontrada = False # Estado para saber si se encontro o no
        
        # Recorro el array de herramientas
        for i in range(0, len(herramientas)):
            if herramientas[i] == nombre_buscado: # Si el nombre buscado coincide con alguno de los nombres almacenados lo muestro
                print(f"Existencias de {herramientas[i]}: {existencias[i]}")
                encontrada = True
                break # Si lo encuentra cierro el ciclo for
        
        if encontrada == False: # Si no lo encuentra muestro un mensaje de error. 
            print("La herramienta buscada no se encuntra en el inventario.")
    
    elif opcion == "5":
        print("\n--- REPORTE DE AGOTADOS ---")
        
        if not herramientas: # Si la lista de herramientas esta vacia imprimo el mensaje en la consola
            print("El listado de herramientas está vacío. \nIngrese a la opción 1 para carga de herramientas.")
        else:
            agotados = []
            
            for i in range(len(existencias)): # Recorro la lista de existencias con un bucle for
                if existencias[i] == 0: # Si encuentro alguna existencia en 0 lo imprimo en la consola
                    agotados.append(herramientas[i])
            if len(agotados) > 0:
                for a in agotados:
                    print(f"La herramienta {a} está agotada.")
            else: # Si en ningun momento se cambia a False, es que no hay ningun elemento agotado
                print("Actualmente todos los productos están en stock.")
                    

    elif opcion == "6":
        print("\n--- ALTA DE NUEVO PRODUCTO ---")
        
        if not herramientas: # Primero verifico si el listado de herramientas está vacio
            print("El listado de herramientas está vacío. \nIngrese a la opción 1 para carga de herramientas.")
            continue
        
        while True: # Esta en un bucle para manejar los errores sin que vuelva al menu inicial
            nuevo_producto = input("Igrese el nombre de la herramienta: ").capitalize() # Pido el nombre del prodcuto
            if not nuevo_producto.isalpha(): # Verifico que sea un string
                print("Error. No puede ingresar un nombre vacío.")
            elif nuevo_producto in herramientas: # Verifico que no est repetido
                print("El producto ingresado ya está en el listado.")
            else:
                cantidad = input("Ingrese la cantidad del nuevo producto: ") # Pido cantidad para las existencias
                if not cantidad.isdigit(): # Si no es numero 
                    print("Error. La cantidad debe ser un numero entero.")
                else: # Si cumple con las condiciones, agrego a lista de herramientas y de existencias
                    herramientas.append(nuevo_producto)
                    existencias.append(int(cantidad))
                    print(f"Producto: {nuevo_producto} agregado al inventario con éxito.")
                    break # Termino el ciclo while
    
    elif opcion == "7":
        print("\n--- ACTUALIZAR STOCK ---")
        
        if not herramientas: # Primero verifico si el listado de herramientas está vacio
            print("El listado de herramientas está vacío. \nIngrese a la opción 1 para carga de herramientas.")
            continue
        
        # Opciones disponibles
        print("1- Venta")
        print("2- Reposicion")
        
        opcion = input("Seleccione la opcion: ")
        if not opcion.isdigit():
            print("Error, la opcion debe ser un número entero.")
        else:
            opcion = int(opcion)
            
        herramienta_actualizar = input("\nIngrese el nombre de la herramienta a actualizar: ").capitalize()
        encontrada = False
        
        for i in range(0, len(herramientas)): # Recorro la lista de herramientas
            if herramientas[i] == herramienta_actualizar: # Si coinciden en nombre, dependiendo de la opcion hago los cambios
                encontrada = True
                if opcion == 1:
                    cantidad = input("Ingrese la cantidad vendida: ") # Pido la cantidad vendida
                    
                    if not cantidad.isdigit():
                        print("Error, la cantidad debe ser un número entero.")
                    else:
                        cantidad = int(cantidad)
                        
                    if cantidad > existencias[i]: # Verifico que las existencias disponibles sean suficientes
                        print("El stock disponible no es suficiente para realizar la venta.")
                    else:
                        existencias[i] = existencias[i] - cantidad # Actualizo el stock
                        print(f"Stock actualizado con éxito. \nLas existencias disponibles del producto {herramientas[i]} es de {existencias[i]}")
                elif opcion == 2:
                    cantidad = input("Ingrese la cantidad a reponer: ") # Pido la cantidad a reponer
                    
                    if not cantidad.isdigit():
                        print("Error, la cantidad debe ser un número entero.")
                    else:
                        cantidad = int(cantidad)
                        
                    if cantidad < 0: # Verifico que la cantidad sea mayor a 0
                        print("La cantidad ingresada debe ser un numero positivo.")
                    else: # Modifico la cantidad de existencias de esa herramienta
                        existencias[i] = existencias[i] + cantidad
                        print(f"Stock modificado con exito. \nLa herramienta {herramientas[i]} tiene en stock {existencias[i]} existencias.")
                else:
                    print("Opción inválida.")
                    break
        
        if encontrada == False: # Si no la encuentra por nombre imprimo un mensaje en pantalla
            print("No se encontró la herramienta seleccionada.")
    
    elif opcion == "8":
        print("\n--- SALIR ---")
        print("Cerrando sistema... ")
        control_menu = False # Paso el controlador del menú a False para cerrar el bucle while
    
    # Else para manejar error si el usuario ingresa una opción inválida
    else:
        print("Opción inválida. Intente nuevamente.")