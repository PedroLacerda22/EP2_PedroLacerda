# Importa as funções do jogo:
from cria_baralho import cria_baralho
from extrai_naipe import extrai_naipe
from extrai_valor import extrai_valor
from possiveis_movimentos import lista_movimentos_possiveis
from empilha import empilha
from possui_movimentos import possui_movimentos_possiveis

deck_do_jogo = cria_baralho()

print("Paciência Acordeão\n")
# Escrever regras do jogo

# Iniciando o jogo:
b_jogo = cria_baralho()
jogando = False
iniciar = int(input("Digite \"1\" para iniciar o jogo: "))
if iniciar == 1: 
    jogando = True

while jogando:
    # Mostrando as cartas para o jogador:
    # esse comando exibe as cartas do baralho exatamente na ordem de b_jogo, porém são mostradas com
    # seu índice e com cores diferentes para uma melhor visualização de seus naipes
    # '♦', '♥', '♣', '♠'
    c_col = []
    for c in b_jogo: # Da a cor de cada naipe

        if "♠" in c: 
            col = "\033[1;34;40m {0}" # Azul
            c_col.append(col.format(c))
        elif "♣" in c:
            col = "\033[1;35;40m {0}" # Magenta
            c_col.append(col.format(c))
        elif "♥" in c: 
            col = "\033[1;31;40m {0}" # Vermelho
            c_col.append(col.format(c))
        elif "♦" in c:
            col = "\033[1;32;40m {0}" # Verde
            c_col.append(col.format(c))

    for a in c_col: # Da o índice de cada carta (comecando em zero)

        indice_da_carta = c_col.index(a)
        if indice_da_carta < 10:
            ind = ("\033[0;37;40m {0}".format(indice_da_carta))
            print(" {0}. ".format(ind) + a)
        else:
            ind = ("\033[0;37;40m {0}".format(indice_da_carta))
            print("{0}. ".format(ind)+ a)
    
    jogando = False