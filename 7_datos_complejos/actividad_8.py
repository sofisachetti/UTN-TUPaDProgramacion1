# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario: 
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe. 

productos = {"Harina": 15, "Arroz": 6, "Azúcar": 8, "Yerba": 13, "Fideos": 5, "Miel": 2}

# Consulta de stock
prod_buscado = input("\nIngrese el producto a consultar: ").capitalize() # Pedir el producto al usuario

# Lógica general la manejo con condicional if/else
if prod_buscado in productos:
    print(f"El stock de {prod_buscado} es de: {productos[prod_buscado]} unidades.") # Si el producto está lo muestro

    opcion = input("\n¿Desea agregar más unidades de este producto? (si / no): ").lower() # Pregunto si quiere agregar más unidades al stock
    
    if opcion == "si":
        cantidad = int(input("\nIngrese la cantidad a agregar (en números enteros): ")) # Solicito la cantidad a agregar
        productos[prod_buscado] += cantidad # Lo sumo al stock ya existente
        print(f"\nEl stock actualizado de {prod_buscado} es de: {productos[prod_buscado]} unidades.")
else:
    opcion = input("\nEl producto buscado no se encuentra en la lista. ¿Desea agregarlo? (si / no): ") # Si el producto no esta, pregunto si lo quiere agregar
    
    if opcion == "si":
        cantidad = int(input("\nIngrese la cantidad del producto (en números enteros): ")) # Solicito la cantidad
        productos[prod_buscado] = cantidad # Lo agrego al diccionario
        print("\n¡Producto agregado con éxito!")
        print(f"{prod_buscado}: {productos[prod_buscado]} unidades")
