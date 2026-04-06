# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

lista = [1, 2, 3, 4, 5, 6, 7]

lista_rotada = [lista[-1]] + lista[:-1]
# hago slicing (saco el ultimo numero) guardandolo en su propia lista y concateno con la lista original excluyendo el ultimo numero

print(lista_rotada)