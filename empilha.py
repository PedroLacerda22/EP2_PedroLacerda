def empilha(l_cartas, pi, pf):
    index1 = l_cartas.index(l_cartas[pi])
    index2 = l_cartas.index(l_cartas[pf])
    l_cartas[index1], l_cartas[index2] = l_cartas[index2], l_cartas[index1]
    l_cartas.remove(l_cartas[pi])
    return l_cartas
