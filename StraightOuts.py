import Deck, Card
from itertools import combinations

# returns card list in sorted in ascending order
def sort(card_list):
    for x in range((len(card_list))):
        for y in range(x+1, (len(card_list)), 1):
            if card_list[x].value > card_list[y].value:
                swap = card_list[x]
                card_list[x] = card_list[y]
                card_list[y] = swap
    return card_list

# returns list of 4 card straights made from possible cards in play and in hand
def get_straights(in_play, in_hand):
    straights = []
    potential_cards = in_play + in_hand
    possible_combinations = list(combinations(potential_cards, 4))
    for entry in possible_combinations:
        entry = sort(list(entry))
        straight = True
        for x in range(3):
            if entry[x].value + 1 != entry[x+1].value:
                straight = False
        if straight:
            straights.append(entry)
    return straights

def print_card_list(card_list):
    print("{0}, {1}, {2}, {3}".format(card_list[0].get_card(), card_list[1].get_card(), card_list[2].get_card(), card_list[3].get_card()))

# returns set of cards that are outs
def get_straight_outs(straights, in_hand, in_play):
    outs = set()
    for straight in straights:
        lower = straight[0]
        #print(lower.get_card())
        upper = straight[-1]
        #print(upper.get_card())
        if lower.value == 2:
            upper_outs = {Card.Card(upper.value+1, "Diamonds"), Card.Card(upper.value+1, "Hearts"), Card.Card(upper.value+1, "Spades"), Card.Card(upper.value+1, "Clubs")}
            outs.update(upper_outs)
        elif upper.value == 14:
            lower_outs = {Card.Card(lower.value-1, "Diamonds"), Card.Card(lower.value-1, "Hearts"), Card.Card(lower.value-1, "Spades"), Card.Card(lower.value-1, "Clubs")}
            outs.update(lower_outs)
        else:
            lower_outs = {Card.Card(lower.value-1, "Diamonds"), Card.Card(lower.value-1, "Hearts"), Card.Card(lower.value-1, "Spades"), Card.Card(lower.value-1, "Clubs")}
            upper_outs = {Card.Card(upper.value+1, "Diamonds"), Card.Card(upper.value+1, "Hearts"), Card.Card(upper.value+1, "Spades"), Card.Card(upper.value+1, "Clubs")}
            outs.update(lower_outs)
            outs.update(upper_outs)
    # need to move this chunk into above loop
    for card in outs:
        if ((card in in_hand) or (card in in_play)):
            outs.remove(card)
    #################
    return outs


#in_deck = Deck.Deck()
in_hand = [Card.Card(7, "Diamonds"), Card.Card(3, "Diamonds")]
#in_hand = []
#in_hand.append(deck.deal())
#in_hand.append(deck.deal())
in_play = [Card.Card(4, "Diamonds"), Card.Card(5, "Diamonds"), Card.Card(6, "Diamonds")]
#in_play = []
#in_play.append(deck.deal())
#in_play.append(deck.deal())
#in_play.append(deck.deal())


print("In Hand: {0}, {1}".format(in_hand[0].get_card(), in_hand[1].get_card()))
print("In Play: {0}, {1}, {2}".format(in_play[0].get_card(), in_play[1].get_card(), in_play[2].get_card()))

straights = get_straights(in_play, in_hand)
print("Straights")
for cards in straights:
    print_card_list(cards)

outs = get_straight_outs(straights, in_hand, in_play)
print("Outs")
for card in outs:
    print(card.get_card())