# Ejercicio 1— “Caja del Kiosco”
# Objetivo: Simular una compra con validaciones y cálculo de total.
# Requisitos
# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while).
# ------------ isdigit() valida sobre string para saber si hay numeros, no sería mejor usar int?
# 3. Por cada producto (usar for):
    # o Pedir precio (entero, validar .isdigit()).
    # o Pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula).
    # o Si tiene descuento: aplicar 10% al precio de ese producto.
# 4. Al final mostrar:
    # o Total sin descuentos
    # o Total con descuentos
    # o Ahorro total
    # o Promedio por producto (usar float y formatear con :.2f, ejem: x = 3.14159 print(f"{x:.2f}"))
# Validaciones obligatorias
    # • Sin try/except.
    # • No aceptar vacío en nombre (si queda vacío, es error).
    # • Cantidad > 0 (si ingresa 0, volver a pedir).


# primera variable es la de nombre para poder dar comienzo al programa
nombre = input("Ingresa tu nombre para comenzar: ") 

# variables de totales inicializadas en 0
total_con_descuento = 0
total_sin_descuento = 0
ahorro = 0
promedio  = 0 

# valido que el nombre sea un string que contenga caracteres 
while nombre.isalpha():
    
    print(f"\n¡Hola {nombre}! Bienvenido al checkout del Kiosco")
    cant_productos = input("Te pedimos que ingreses la cantidad de productos que vas a comprar: ") # usar int?
    
    while cant_productos.isdigit() and cant_productos != "0": # uso la funcion para saber si el string ingresado contiene numeros
        cant_productos = int(cant_productos) # paso el string a numero entero para poder usarlo dentro del for
        
        for p in range(1, cant_productos + 1):
            precio = int(input(f"\nIngresa el precio del producto {p}: "))
            total_sin_descuento += precio # tomo los precios originales para almacenarlos y saber cuanto es el total sin descuentos
            tiene_descuento = input("¿Este producto tiene descuento? Responde con S o N: ").upper() #uso upper() para que si el usuario ingresa mayusc. o minusc. ingrese siempre con el mismo formato
            
            # Mientras descuento sea true aplico los calculos para saber valor del descuento, total del precio y ahorro
            while tiene_descuento == "S":
                valor_descuento = precio * 10 / 100 # calculo cuanto hay de descuento
                precio = precio - valor_descuento  # calculo el precio final del producto con el descuento
                ahorro += valor_descuento
                print(f"Precio final del producto con el descuento del 10%: ${precio}")
                break # break para terminar con el bucle de descuento si no hay que aplicarlo
            
            total_con_descuento += precio # sumo el total de los precios con y sin descuento
            promedio = total_sin_descuento / cant_productos # calculo el promedio de precios
        # detalle de los resultados impresos en consola
        print("\n--- DETALLE DE SU COMPRA ---\n")
        print(f"Total sin descuento: ${total_sin_descuento}")
        print(f"Total con descuento: ${total_con_descuento}")
        print(f"Ahorro total: ${ahorro}")
        print(f"Promedio de precio por producto: ${promedio:.2f}")
        break
    
    break # break para que una vez que se complete el bucle principal del nombre no se vuelva a ejecutar