'''
2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
'''
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        producto = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        
        print(f"Poducto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")