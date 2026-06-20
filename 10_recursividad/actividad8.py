'''
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4 
'''
def contar_digito(numero, digito):
    if numero == 0:  # caso base
        return 0

    if numero % 10 == digito:  # verifica el ultimo digito
        return 1 + contar_digito(numero // 10, digito)

    return contar_digito(numero // 10, digito)  # recursividad

numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese un dígito a buscar: "))
print("Cantidad de apariciones:", contar_digito(numero, digito))