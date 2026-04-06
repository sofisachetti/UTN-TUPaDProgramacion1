# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# ● Inicializarlo con guiones "-" representando casillas vacías.
# ● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# ● Mostrar el tablero después de cada jugada.

# tablero inicial vacio
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# variable para guardar el turno, empieza con el turno del X
turno = "X"

# logica principal, con el for recorro la cantidad de jugadas que puede haber: tablero de 3*3 = total de 9 jugadas
for _ in range(9): 
    # empiezo mostrando el tablero
    for fila in tablero:
        print(" ".join(fila)) # para que se imprima "formateado" y no con los corchetes de lista
    print() # salto de linea
    
    print("Turno del jugador", turno) # indico a quien le toca el turno
    # guardo la seleccion del usuario para su lugar
    fila = int(input("Ingrese fila (0-2): ")) 
    col = int(input("Ingrese columna (0-2): "))
    
    # valido si la casilla est libre
    if tablero[fila][col] == "-":
        tablero[fila][col] = turno
        
        # intercambio los turnos
        if turno == "X":
            turno = "O"
        else:
            turno = "X"
    else:
        print("Casilla ocupada, intente de nuevo")

# muestro el tablero al final
for fila in tablero:
    print(" ".join(fila))