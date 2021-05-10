# Novo plano é tentar fazer o jogo funcionar antes de implementar as coisasque fazem ele ficar bonito.

# Importa as bibliotecas necessárias:
from cria_baralho import cria_baralho as cb # funcionando; args=(), retorna umbaralho de 52 cartas em ordem aleatória
from extrai_naipe import extrai_naipe as ex_np # funcionando; args=(carta) retorna o naipe de uma carta
from extrai_valor import extrai_valor as ex_val # funcionando; args=(carta) retorna o valor numérico de uma carta
from possiveis_movimentos import lista_movimentos_possiveis as mov_pos # funcionando; args=(baralho, índice) retorna os movimentos possíveis para uma determinada carta
from empilha import empilha as emp # funcionando mas tá um pouco confuso; args=(baralho, posição inicial, posição de destino), retorna o baralho após o empilhamento de uma carta
# A função que checa se ainda existem movimentos no baralho retorna False quando implementada agora. Ela será chamada posteriormente.

# Agora para iniciar o jogo:

jogando = False
print('PACIÊNCIA ACORDEÃO\n')
iniciar = int(input("Para iniciar o jogo, digite 1: "))

if iniciar == 1:
    jogando = True
    b_jogo = cb()
else:
    jogando == False

while jogando:

    # Para mostrar uma carta por linha, mostrando seu respectivo índice:

    for carta in b_jogo:
        indice_da_carta = b_jogo.index(carta)
        if indice_da_carta < 10: 
            ind = " {0}. ".format(indice_da_carta)
        else:
            ind = "{0}. ".format(indice_da_carta)

        valor_da_carta = ex_val(carta)
        if valor_da_carta == "10":
            print(ind + carta)
        else:
            print(ind + " " + carta)


    escolha = input('Digite o que você deseja fazer:')
    if escolha != "continuar":
        jogando = False
        print("\nFim do Jogo")
    # O display das cartas no terminal está funcionando normalmente. 
    # Posteriormente eu vou implementar as cores das cartas de acordo com seu respectivo naipe.

    # Agora a próxima etapa é dar decisões ao jogador:
    # a função "possui movimentos" será executado. Caso retorne True, o jogo continua. Caso retorne False,
    # o jogo acaba.