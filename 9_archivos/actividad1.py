'''
1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
'''
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,450,15\n")
    archivo.write("Lápiz,100,25\n")