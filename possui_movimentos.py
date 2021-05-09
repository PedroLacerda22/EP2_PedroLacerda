from possiveis_movimentos import lista_movimentos_possiveis

def possui_movimentos_possiveis(deck):
    movimentos = []
    for card in deck:
        m = lista_movimentos_possiveis(deck, deck.index(card))
        movimentos.append(m)
    
    for j in movimentos:
        if len(j) > 0:
            return True
    else: 
        return False
print(possui_movimentos_possiveis(['A♦', '10♥', 'Q♣', '4♠']))