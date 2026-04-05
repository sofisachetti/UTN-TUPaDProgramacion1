# 2) Pedir al usuario que cargue 5 productos en una lista.
# ● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# ● Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = [] #inicializo la lista vacia

# con bucle while pido al usuario los productos, mientras que la longitud de la lista sea menor a 5 [0, 1, 2, 3, 4]
while len(productos) < 5: 
    producto = input("Ingrese un producto: ").lower() # paso todos los productos a minuscula para que no haya problema a la hora de borrar
    productos.append(producto) # con cada vuelta voya gregando los productos a la lista
prod_ordenados = sorted(productos) # los ordeno alfabeticamente con sorted()

print("\nLista de productos ordenada alfabeticamente:") # imprimo la lista ordenada con un bucle for
for prod in prod_ordenados:
    print(prod)

# verificacion para eliminar un producto
conf = input("\n¿Desea eliminar algún producto de la lista? (Si/No): ").upper()
if conf == "SI":
    prod_eliminar = input("Ingrese el producto a eliminar: ").lower() # pido el producto a eliminar
    if prod_eliminar in prod_ordenados: # verifico que el prod este dentro de la lista
        prod_ordenados.remove(prod_eliminar) # si esta lo elimino con remove()
        print(f"Producto eliminado con exito!")
        print("\nLista de productos final:") # imprimo la lista final con un elemento menos
        for prod in prod_ordenados:
            print(prod)
    else:
        print("El producto ingresado no está en la lista.")

