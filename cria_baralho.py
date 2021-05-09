# Função que cria e embaralha as cartas #

def cria_baralho():
    import random
    cartas = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠',
    '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',
    '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
    '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣']
    cartas_coloridas = []
    for c in cartas:
        if "♠" in c:
            col = "\033[1;30;40m {0}"
            cartas_coloridas.append(col.format(c))
        elif "♥" in c:
            col = "\033[1;31;40m {0}"
            cartas_coloridas.append(col.format(c))
        elif "♦" in c:
            col = "\033[1;31;40m {0}"
            cartas_coloridas.append(col.format(c))
        elif "♣" in c:
            col = "\033[1;30;40m {0}"
            cartas_coloridas.append(col.format(c))

    random.shuffle(cartas_coloridas)
    
    for item in cartas_coloridas:
        ic = cartas_coloridas.index(item)
        if ic <= 9:
            ind_cartas = ("\033[0;37;40m  {0}".format(ic))
            print("{0}. ".format(ind_cartas) + item)
        else:
            ind_cartas = ("\033[0;37;40m {0}".format(ic))
            print("{0}. ".format(ind_cartas) + item)
    

print(cria_baralho())