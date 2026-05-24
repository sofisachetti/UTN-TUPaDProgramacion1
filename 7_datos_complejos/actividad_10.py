# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores. 

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}

# Desestructuro los items del diccionario
for pais, capital in original.items():
    invertido[capital] = pais # lo almaceno invertido en el otro diccionario

print("\nDiccionario original: ")
print(original)

print("\nDiccionario invertido: ")
print(invertido)