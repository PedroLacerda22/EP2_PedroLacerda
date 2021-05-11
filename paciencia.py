# Importa as funções necessárias:

from cria_baralho import cria_baralho as cb # funcionando; args=(), retorna um baralho de 52 cartas em ordem aleatória
from possiveis_movimentos import lista_movimentos_possiveis as mov_pos # funcionando; args=(baralho, índice) retorna os movimentos possíveis para uma determinada carta
from empilha import empilha as emp # funcionando; args=(baralho, posição inicial, posição de destino), retorna o baralho após o empilhamento de uma carta
from mostra_baralho import mostra_cartas as mc # funionando; args=(baralho), mostra o baralho no terminal

# Agora para iniciar o jogo:
tem_movimentos = True
jogando = False
print('Bem vindo ao jogo de Paciência Acordeão\n')

print("As regras do jogo são as seguintes:")
print("As cartas só podem der movimentadas para duas posições:")
print("- Seu 1º vizinho anterior ou\n- Seu 3º vizinho anterior\n")
print("O movimento das cartas só é permitido se as duas cartas:")
print("- São do mesmo naipe ou\n- Têm o mesmo valor numérico\n")
print("O jogador vence quando resta apenas uma carta no jogo.")
print("Caso não existam movimentos possíveis ou o jogador digitar zero (0) como o índice da carta, o jogo é encerrado.\n")

iniciar = int(input("Para iniciar o jogo, digite 1: "))

if iniciar == 1:
    jogando = True
    b_jogo = cb()
else:
    jogando = False

from possui_movimentos import possui_movimentos_possiveis as t_mov # funcionando; args=(baralho)
while jogando:
    
    # Define a condição de fim de jogo
    tem_movimentos = t_mov(b_jogo)
    if not tem_movimentos:
        jogando = False
        print('Sem movimentos restantes. Fim do jogo.')
    
    if len(b_jogo) == 1:
        jogando = False
        print("Você venceu!")
    # Para mostrar uma carta por linha, mostrando seu respectivo índice:

    print(mc(b_jogo))

    selecao = True
    while selecao:
        # digitar zero p/ encerrar o jogo
        indice_carta = int(input('Digite o indice carta que quer movimentar: ')) -1
        if indice_carta == -1:
            # Jogador escolheu acaba o jogo
            jogando = False
            print("\nFim do Jogo")
        
        elif indice_carta in range(0, len(b_jogo)):
            # Selecionou um índice
            indice_carta_mov = mov_pos(b_jogo, indice_carta)

            if len(indice_carta_mov) == 0: # funcionando
                # Se for a primeira carta, não da pra 
                print(mc(b_jogo))
                print('Não é possivel mover essa carta.')
                
            elif len(indice_carta_mov) == 1:
                # Se a função mov_pos retornou uma lista com só um item:
                if indice_carta_mov[0] == 1:
                    # Se só é possível mover a carta para o vizinho anterior
                    b_novo = emp(b_jogo, indice_carta, b_jogo.index(b_jogo[indice_carta]) - 1)
                    b_jogo = b_novo
                    print(mc(b_jogo))
                    print("A carta foi empilhada em seu vizinho anterior")
                    
                    # A carta é automaticamente empilhada e o baralho é atualizado de acordo.

                elif indice_carta_mov[0] == 3:
                    b_novo = emp(b_jogo, indice_carta, b_jogo.index(b_jogo[indice_carta]) - 3)
                    b_jogo = b_novo
                    print(mc(b_jogo))
                    print("A carta foi empilhada em seu 3º vizinho anterior")
                    # A carta é automaticamente empilhada e o baralho é atualizado de acordo.

            elif len(indice_carta_mov) == 2:
                # Se a função mov_pos tem mais de 1 item na lista:
                print("Essa carta pode ser empilhada nas posições anteriores [1, 3].")
                qual_emp = int(input("Digite em qual das cartas você quer empilhar: "))
                # O jogador pode escolher em qual vizinho a cara será empilhada.

                if qual_emp == 1:
                    b_novo = emp(b_jogo, indice_carta, b_jogo.index(b_jogo[indice_carta]) - 1)
                    b_jogo = b_novo
                    print(mc(b_jogo))
                    print("A carta foi empilhada em seu vizinho anterior")

                elif qual_emp == 3:
                    b_novo = emp(b_jogo, indice_carta, b_jogo.index(b_jogo[indice_carta]) - 3)
                    b_jogo = b_novo
                    print(mc(b_jogo))
                    print("A carta foi empilhada em seu 3º vizinho anterior")

                    # talvez de pra encurtar esses if elif statements.
                else:
                    print(mc(b_jogo))
                    print("Entrada invalida.")

    # o stacking não esá funcionando para empilhar uma carta sobre uma outra carta de valor 10. A operação funciona normalmente no outro sentido