import StraightOuts

def board_connectivity(in_play):
    sorted = StraightOuts.sort(in_play)
    connects = 0
    for i in range(0, len(sorted)):
        if i + 1 >= len(sorted):
            break
        if sorted[i].value + 1 == sorted[i + 1].value:
            connects += 1
            if connects == 3:
                return True
        else:
            connects = 0
    return False

def board_tone(in_play):
    diamonds = 0
    hearts = 0
    clubs = 0
    spades = 0
    for card in in_play:
        if card.suit == "Diamonds":
            diamonds += 1
        elif card.suit == "Hearts":
            hearts += 1
        elif card.suit == "Clubs":
            clubs += 1
        elif card.suit == "Spades":
            spades += 1
    
    tone = {}
    if diamonds > 2:
        tone["Diamonds"] = diamonds
    if hearts > 2:
        tone["Hearts"] = hearts
    if clubs > 2:
        tone["Clubs"] = clubs
    if spades > 2:
        tone["Spades"] = spades
    
    return tone

