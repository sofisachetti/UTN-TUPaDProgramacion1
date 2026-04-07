# 13) Dada la siguiente lista de puntajes de un videojuego:
# ● Mostrar el puntaje más alto y el más bajo.
# ● Mostrar la lista ordenada de mayor a menor (ranking).
# ● Indicar en qué posición del ranking se encuentra el puntaje 990.

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# mas alto y mas bajo, uso metodos max() y min()
mayor = max(puntajes)
menor = min(puntajes)
print("Puntaje más alto:", mayor)
print("Puntaje más bajo:", menor)

# ranking desc.
ranking = sorted(puntajes, reverse=True)
print("Ranking:", ranking)

# posicion del puntaje
for i in range(len(ranking)):
    if ranking[i] == 990:
        print(f"El puntaje 990 está en la posición: {i}")
        break
