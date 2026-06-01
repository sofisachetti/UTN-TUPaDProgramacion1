'''
3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.
'''
print("\n------- Carga manual -------\n")
nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")