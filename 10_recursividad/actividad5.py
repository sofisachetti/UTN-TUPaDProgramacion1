'''
Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
'''

def es_palindromo(palabra):
    if len(palabra) <= 1:  # caso base: cuando la palabra ya tiene una sola letra
        return True

    if palabra[0] != palabra[-1]:  # verifica si la palabra empieza y termina con la misma letra
        return False

    return es_palindromo(palabra[1:-1]) # recusrsividad: le va sacando las letras de principio y fin, sigue comparando

texto = input("Ingrese una palabra: ")
if es_palindromo(texto):
    print("Es palíndromo")
else:
    print("No es palíndromo")