'''
4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.
'''
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(producto)


'''
5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.
'''

buscado = input("Ingrese el producto a buscar: ")
encontrado = False

for producto in productos:
    if producto["nombre"].lower() == buscado.lower():
        print("Producto encontrado")
        print("Nombre:", producto["nombre"])
        print("Precio:", producto["precio"])
        print("Cantidad:", producto["cantidad"])

        encontrado = True
        break

if not encontrado:
    print("Error: producto no encontrado")


'''
6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.
'''
with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = (f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
        archivo.write(linea)