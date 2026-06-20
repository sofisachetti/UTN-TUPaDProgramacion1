'''
Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)
'''

def contar_bloques(num):
    if num == 1:  # cuando llega al fin de la piramide solo hay un bloque
        return 1

    return num + contar_bloques(num - 1) # el caso recursivo es num de bloques mas num de bloques menos uno

nivel = int(input("Cantidad de bloques en la base: "))
print("Total:", contar_bloques(nivel))
