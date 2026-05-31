# 1) Identifica los errores del código usando comentarios (#) en las líneas afectadas. Indica el tipo
# de error y una breve explicación de por qué ocurre.

# ----- Código original -----
a = 10
b = input("Introduce un número: ")
result = a / b      
print(f"Resultado: {result}")
# Este bloque lanzaría un TypeError. 
# Los errores de tipo ocurren cuando intentamos hacer operaciones con elementos que no son compatibles. 
# En este caso, se intenta realizar una división entre un número entero (a) y un string (b). 
# Al ser b una variable que ingresa por un input, esta va a ingresar en tipo string, lo que haría imposible realizar la operación matemática.

numbers = [1, 2, 3]
print(numbers[5])
# El error de este bloque es un IndexError. 
# Intentar ingresar a un índice que está por fuera del rango definido (como number[5]) daría como resultado este tipo de error,
# ya que en la lista declarada numbers solo hay 3 índices (0, 1, 2).


# 2) Utilizando el código del ejercicio 1, arreglar los errores para que la ejecución del programa
# sea correcta sin necesidad de usar excepciones.

a = 10
b = int(input("Introduce un número: "))
result = a / b      
print(f"Resultado: {result}")

numbers = [1, 2, 3]
print(numbers[2])


# 3) Utilizando el código del ejercicio 1, mantener el código con los errores originales e incluir
# bloques try-except para que la ejecución del programa no se frene al encontrar los errores.

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b
    print(f"Resultado: {result}")
except:
    print("Ha ocurrido un error: no se puede ejecutar la operación.")

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except:
    print("Ha ocurrido un error: no se puede acceder al ínidce.")


# 4) Repetir el ejercicio 3, pero usando excepciones múltiples que hagan alusión a los tipos de
# errores detectados.

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b
    print(f"Resultado: {result}")
except TypeError:
    print("Error: utilización de tipos diferentes.")
except ZeroDivisionError:
    print("Error: No puede dividir por 0.")
except ValueError:
    print("Error: debe ingresar un número válido.")

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Ha ocurrido un error: no se puede acceder al ínidce.")


# 5) Repetir el ejercicio 4, pero esta vez incluyendo bloques else y finally.

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / int(b)
    print(f"Resultado: {result}")
except TypeError:
    print("Error: utilización de tipos diferentes.")
except ZeroDivisionError:
    print("Error: No puede dividir por 0.")
except ValueError:
    print("Error: debe ingresar un número válido.")
else:
    print("Ejecución exitosa.")
finally:
    print("Programa finalizado.")

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Ha ocurrido un error: no se puede acceder al ínidce.")
else:
    print("Ejecución exitosa.")
finally:
    print("Programa finalizado.")
