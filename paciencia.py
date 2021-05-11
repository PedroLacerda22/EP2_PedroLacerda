# Novo plano é tentar fazer o jogo funcionar antes de implementar as coisasque fazem ele ficar bonito.

# Importa as bibliotecas necessárias:
from cria_baralho import cria_baralho as cb # funcionando; args=(), retorna umbaralho de 52 cartas em ordem aleatória
from extrai_naipe import extrai_naipe as ex_np # funcionando; args=(carta) retorna o naipe de uma carta
from extrai_valor import extrai_valor as ex_val # funcionando; args=(carta) retorna o valor numérico de uma carta
from possiveis_movimentos import lista_movimentos_possiveis as mov_pos # funcionando; args=(baralho, índice) retorna os movimentos possíveis para uma determinada carta
from empilha import empilha as emp # funcionando mas tá um pouco confuso; args=(baralho, posição inicial, posição de destino), retorna o baralho após o empilhamento de uma carta
# A função que checa se ainda existem movimentos no baralho retorna False quando implementada agora. Ela será chamada posteriormente.

# Agora para iniciar o jogo:

tem_movimentos = True
jogando = False
print('PACIÊNCIA ACORDEÃO\n')
iniciar = int(input("Para iniciar o jogo, digite 1: "))

if iniciar == 1:
    jogando = True
    b_jogo = cb()
else:
    jogando == False

from possui_movimentos import possui_movimentos_possiveis as t_mov # status?
while jogando:
    
    # Define a condição de fim de jogo
    tem_movimentos = t_mov(b_jogo)
    if not tem_movimentos:
        jogando = False
        print('Sem movimentos restantes. Fim do jogo.')
    # Para mostrar uma carta por linha, mostrando seu respectivo índice:

    for carta in b_jogo:
        indice_da_carta = b_jogo.index(carta)
        if indice_da_carta < 10: 
            ind = " {0}. ".format(indice_da_carta + 1)
        else:
            ind = "{0}. ".format(indice_da_carta + 1)

        valor_da_carta = ex_val(carta)
        if valor_da_carta == "10":
            print(ind + carta)
        else:
            print(ind + " " + carta)

    selecao = True
    while selecao:
        # digitar zero p/ encerrar o jogo
        indice_carta = int(input('Digite o indice carta que quer movimentar: ')) -1
        if indice_carta == -1:
            # Jogador escolheu acaba o jogo
            jogando = False
            print("\nFim do Jogo")
        
        elif indice_carta in range(0, len(b_jogo)+1):
            # Selecionou um índice
            indice_carta_mov = mov_pos(b_jogo, indice_carta)

            if len(indice_carta_mov) == 0: # funcionando
                # Se for a primeira carta, não da pra mover
                print('Não é possivel mover essa carta.')

            elif len(indice_carta_mov) == 1:
                # Se a função mov_pos retornou uma lista com só um item:

                if indice_carta_mov[0] == 1:
                    # Se só é possível mover a carta para o vizinho anterior
                    b_novo = emp(b_jogo, indice_carta, b_jogo.index(b_jogo[indice_carta]) - 1)
                    b_jogo = b_novo
                    print(b_jogo)
                    print("A carta foi empilhada em seu vizinho anterior")
                    
                    # A carta é automaticamente empilhada e o baralho é atualizado de acordo.

                elif indice_carta_mov[0] == 3:
                    b_novo = emp(b_jogo, indice_carta, b_jogo.index(b_jogo[indice_carta]) - 3)
                    b_jogo = b_novo
                    print(b_jogo)
                    print("A carta foi empilhada em seu 3º vizinho anterior")
                    # A carta é automaticamente empilhada e o baralho é atualizado de acordo.

            elif len(indice_carta_mov) == 2:
                # Se a função mov_pos tem mais de 1 item na lista:
                print("Essa carta pode ser empilhada nas posições anteriores [1, 3].")
                qual_emp = int(input("Digite em qual das cartas você quer empilhar: "))
                # O jogador pode escolher em qual vizinho a cara será empilhada.

                if qual_emp == 1:
                    b_novo = emp(b_jogo, b_jogo.index(indice_carta), b_jogo.index(b_jogo[indice_carta]) - 1)
                    b_jogo = b_novo
                    print(b_jogo)
                    print("A carta foi empilhada em seu vizinho anterior")

                elif qual_emp == 3:
                    b_novo = emp(b_jogo, indice_carta, b_jogo.index(b_jogo[indice_carta]) - 3)
                    b_jogo = b_novo
                    print(b_jogo)
                    print("A carta foi empilhada em seu 3º vizinho anterior")

                    # talvez de pra encurtar esses if elif statements.
                else:
                    print("Entrada invalida.")

    # Por enquanto, a continuidade do jogo está funcionando bem. Mas é preciso implemenetar uma função que mostra o baralho (1 carta por linha)
    # de modo com que possa ser chamada após o fim de cada uma das decisões.
    # Atualmente, ao final da primeira decisão o código imprime a lista de cartas ao invés de cada uma por linha juntamente ao seus índices.