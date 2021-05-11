def lista_movimentos_possiveis(baralho, index):
    from extrai_naipe import extrai_naipe as ex_np
    from extrai_valor import extrai_valor as ex_val
    c_sel = baralho[index] # carta selecionada do baralho
    val_carta = ex_val(c_sel)
    v1 = ex_val(baralho[index - 1])
    v3 = ex_val(baralho[index - 3])
    np_carta = ex_np(c_sel)
    n1 = ex_np(baralho[index - 1])
    n3 = ex_np(baralho[index - 3])

    if index == 0: # se o indice da carta é igual a zero, não há movimentos possíveis
        return []

    elif index <= 2: # para as 3 primeiras cartas do baralho
        if val_carta == v1:
            return [1]
        elif np_carta == n1:
            return [1]
        else:
            return []

    elif index > 2:
        p_mov = []
        if val_carta == v1:
            # msm valor 1
            p_mov.append(1)
        elif np_carta == n1:
            # msm naipe 1
            p_mov.append(1)
        
        if val_carta == v3:
            # msm valor 3
            p_mov.append(3)
        elif np_carta == n3:
            # msm naipe 3
            p_mov.append(3)

        return p_mov