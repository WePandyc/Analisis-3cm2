def torre(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mueve el disco 1 desde la torre {origen} a la torre {destino}")
        return
    torre(n - 1, origen, destino, auxiliar)
    print(f"Mueve el disco {n} desde la torre {origen} a la torre {destino}")
    torre(n - 1, auxiliar, origen, destino)

n = 5
torre(n, 'A', 'B', 'C')
