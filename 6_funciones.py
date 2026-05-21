# Trabajo Práctico N°6: Funciones en Python
# Materia: Programación 1 - Tecnicatura Universitaria en Programación a Distancia
# Alumna: Sofía Sachetti


# ----- ACTIVIDAD 1 -----
# Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
# Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# ----- ACTIVIDAD 2 -----
# Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. 
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    if nombre.isalpha(): # verifico que se ingrese un string
        print(f"Hola {nombre}!")
    else:
        print("Debe ingresar una cadena de texto.")

nombre_usuario = input("Ingrese su nombre: ").capitalize() # para que el nombre que ingresa comience con mayúscula
saludar_usuario(nombre_usuario)


# ----- ACTIVIDAD 3 -----
# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    if nombre.isalpha() and apellido.isalpha() and edad.isdigit() and residencia.isalpha():
        print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    else:
        print("Algún dato fue ingresado de forma incorrecta.")

nombre_usuario_2 = input("Ingrese su nombre: ").capitalize()
apellido_usuario = input("Ingrese su apellido: ").capitalize()
edad_usuario = input("Ingrese su edad: ")
residencia_usuario = input("Ingrese su lugar de residencia: ").capitalize()
informacion_personal(nombre_usuario_2, apellido_usuario, edad_usuario, residencia_usuario)


# ----- ACTIVIDAD 4 -----
# Crear dos funciones: 
# calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    if radio.isdigit():
        radio = float(radio)
        area = 3.14 * (radio ** 2)
        return area
    else:
        print("Número ingresado inválido.")

def calcular_perimetro_circulo(radio):
    if radio.isdigit():
        radio = float(radio)
        perimetro = 2 * 3.14 * radio
        return perimetro
    else:
        print("Número ingresado inválido.")

radio = input("Ingrese el radio del círculo en centímetros: ")
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es de {area} cm. y su perímetro es de {perimetro} cm.")


# ----- ACTIVIDAD 5 -----
# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro 
# y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    if segundos.isdigit():
        segundos = int(segundos)
        horas = segundos / 3600
        return horas
    else:
        print("Número ingresado inválido.")

segundos = input("Ingrese la cantidad de segundos: ")
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")


# ----- ACTIVIDAD 6 -----
# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e
# imprima la tabla de multiplicar de ese número del 1 al 10. 
# Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    if numero.isdigit():
        numero = int(numero)
        print(f"Tabla de multiplicar del número {numero}: ")
        for i in range(1, 11):
            resultado = i * numero
            print(f"{i} x {numero} = {resultado}")
    else: 
        print("Número ingresado inválido.")

numero = input("Ingrese un número para ver su tabla de multiplicar: ")
tabla_multiplicar(numero)


# ----- ACTIVIDAD 7 -----
# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla 
# con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        if b == 0:
            print("No se puede dividir por 0.")
        else:
            division = a / b
        return suma, resta, multiplicacion, division

num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

print(f"Los resultados de las operaciones básicas con los números {num1} y {num2} son:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


# ----- ACTIVIDAD 8 -----
# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es de: {imc:.2f}")


# ----- ACTIVIDAD 9 -----
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una
# temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")


# ----- ACTIVIDAD 10 -----
# Crear una función llamada calcular_promedio(a, b, c) que reciba tres
# números como parámetros y devuelva el promedio de ellos. Solicitar los
# números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio es de: {promedio:.2f}")