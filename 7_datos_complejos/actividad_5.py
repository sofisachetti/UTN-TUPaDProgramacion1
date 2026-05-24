# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra. 

frase = input("Ingrese su frase: ")

palabras = frase.lower().split() # guardo las palabras de la frase en una lista

palabras_unicas = set(palabras) # creo un set con el array de palabras

print("\nPalabras únicas de la frase:")
print(palabras_unicas)


# Diccionario con contador
contador_palabras = {}

# Con el for recorro la lista de palabras
for i in palabras:
    if i in contador_palabras: # Si la iteración ya está en el contador, le sumo uno al contador
        contador_palabras[i] += 1
    else:
        contador_palabras[i] = 1 # Si la iteración no está previamente en el contador, le asigno uno

print("\nCantidad de veces que se repiten las palabras en la frase: ")
print(contador_palabras)