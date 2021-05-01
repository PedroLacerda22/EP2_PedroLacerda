# Função que extrai o valor da carta #

def extrai_valor(carta):
    if 'A' in carta:
        return 'A'
    elif 'K' in carta:
        return 'K'
    elif 'Q' in carta:
        return 'Q'
    elif 'J' in carta:
        return 'J'
    elif '10' in carta:
        return '10'
    elif '9' in carta:
        return '9'
    elif '8' in carta:
        return '8'
    elif '7' in carta:
        return '7'
    elif '6' in carta:
        return '6'
    elif '5' in carta:
        return '5'
    elif '4' in carta:
        return '4'
    elif '3' in carta:
        return '3'
    elif '2' in carta:
        return '2'

