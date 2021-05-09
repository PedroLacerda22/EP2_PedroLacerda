def lista_movimentos_possiveis(baralho, index):
    c_sel = baralho[index]

    if index == 0:
        return []
    elif index <= 2:
        if len(c_sel) == 3:
            if "10" in baralho[index - 1]:
                # carta anterior é 10
                return [1]
            elif baralho[index - 1][-1] == c_sel[-1]:
                # msm naipe da anterior
                return [1]
            else:
                return []

        if baralho[index - 1][0] == c_sel[0]:
            # msm valor
            return [1]
        elif baralho[index - 1][1] == c_sel[1]:
            # msm naipe
            return [1]
        else:
            return []

    elif index > 2:
        p_mov = []
        if len(c_sel) == 3:
            if "10" in baralho[index - 1]:
                # msm valor 1
                p_mov.append(1)
            elif baralho[index - 1][-1] == c_sel[-1]:
                # msm naipe 1
                p_mov.append(1)

            if "10" in baralho[index - 3]:
                # msm valor 3
                p_mov.append(3)
            elif baralho[index - 3][-1] == c_sel[-1]:
                # msm naipe 3
                p_mov.append(3)

            return p_mov

        elif baralho[index - 1][0] == c_sel[0]:
            # msm valor 1
            p_mov.append(1)
        elif baralho[index - 1][1] == c_sel[1]:
            # msm naipe 1
            p_mov.append(1)

        if baralho[index - 3][0] == c_sel[0]:
            # msm valor 3
            p_mov.append(3)
        elif baralho[index - 3][1] == c_sel[1]:
            # ms naipe 3
            p_mov.append(3)
        else: 
            return p_mov

        return p_mov