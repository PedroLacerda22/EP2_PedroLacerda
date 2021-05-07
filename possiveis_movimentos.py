def lista_movimetos_possiveis(baralho, indice):
    c_sel = baralho[indice]
    if indice == 0:
        return []
    elif indice == 1:
        if c_sel[0] == baralho[0][0]:
            # msm valor:
            return [1]
        elif c_sel[1] == baralho[0][1]:
            # msm naipe:
            return [1]
        else:
            return []

    elif indice == 2:
        if c_sel[0] == baralho[1][0]:
            # msm valor
            return [1]
        elif c_sel[1] == baralho[1][1]:
            # msm naipe
            return [1]
        else:
            return []

    elif indice == 3:
        l = []
        if c_sel[0] == baralho[2][0]:
            # msm valor do vizinho anterior
            l.append(1)
        elif c_sel[0] == baralho[0][0]:
            # msm valor do 3º vizinho anterior
            l.append(1)
        if c_sel[1] == baralho[2][1]:
            # msm naipe do vizinho anterior
            l.append(3)
        elif c_sel[1] == baralho[0][1]:
            # msm naipe do 3º vizinho anterior     
            l.append(3)  

        return l
