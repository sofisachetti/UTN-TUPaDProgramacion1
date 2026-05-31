# 6) Escribir un programa que pida al usuario un número, y:
# ● Si el valor ingresado es válido, lo imprima por pantalla.
# ● Si el valor ingresado no es numérico, imprima por pantalla “Debe ingresar un número válido”.
# ● Si contiene algún otro tipo de error, imprima por pantalla “Se produjo un error inesperado” junto con el error que surgió.

try: 
    num = int(input("Ingrese un número: "))
    print("Su número es: ", num)
except ValueError:
    print("Debe ingresar un número válido.")
except Exception as e:
    print("Se produjo un error inesperado: ", type(e).__name__)


# 7) Repetir el ejercicio 6, pero añadiendo la posibilidad de que el usuario intente ingresar un
# nuevo número luego de encontrar un error.

while True:
    try: 
        num = int(input("Ingrese un número: "))
        print("Su número es: ", num)
        break
    except ValueError:
        print("Debe ingresar un número válido. Intente nuevamente.")
    except Exception as e:
        print("Se produjo un error inesperado: ", type(e).__name__)