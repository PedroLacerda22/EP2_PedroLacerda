def mostra_cartas(baralho_atual):
    from extrai_naipe import extrai_naipe as ex_np
    from extrai_valor import extrai_valor as ex_val
    c_col = [] # cartas coloridas 

    for c_branca in baralho_atual:
        # Primeiramente, para determinar a cor da carta:
        naipe_da_carta = ex_np(c_branca)
        if naipe_da_carta == '♦':
            col ="\033[1;34;40m {0}" # Azul
            c_col.append(col.format(c_branca))

        elif '♥' == naipe_da_carta:
            col = "\033[1;31;40m {0}" # Vermelho
            c_col.append(col.format(c_branca))

        elif '♣' == naipe_da_carta:
            col = "\033[1;32;40m {0}" # Verde
            c_col.append(col.format(c_branca))

        elif '♠' == naipe_da_carta:
            col = "\033[1;35;40m {0}" # Magenta
            c_col.append(col.format(c_branca))

    for c in c_col: # Da o indice da carta, formatada prorpiamente e com a cor padrão
        indice_da_carta = c_col.index(c)
        if indice_da_carta < 9:
            ind = "\033[0;37;40m {0}. ".format(indice_da_carta + 1)
        else:
            ind = "\033[0;37;40m{0}. ".format(indice_da_carta + 1)

        valor_da_carta = ex_val(c)
        if valor_da_carta == '10':
            print(ind + c)
        else:
            print(ind + " " + c)

    txt_normal = "\033[0;37;40m " # Volta a mostrar o texto na cor normal.
    return txt_normal