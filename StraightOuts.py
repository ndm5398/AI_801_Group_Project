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
    card_list = list(card_list)
    if len(card_list) == 4:
        print("{0}, {1}, {2}, {3}".format(card_list[0].get_card(), card_list[1].get_card(), card_list[2].get_card(), card_list[3].get_card()))
    if len(card_list) == 5:
        print("{0}, {1}, {2}, {3}, {4}".format(card_list[0].get_card(), card_list[1].get_card(), card_list[2].get_card(), card_list[3].get_card(), card_list[4].get_card()))

def compare_card(card_1, card_2):
    if ((card_1.value == card_2.value) and (card_1.suit == card_2.suit)):
        return True
    else:
        return False

# returns set of cards that are outs
def get_straight_outs(straights, in_hand, in_play):
    outs = set()
    potential_cards = in_play + in_hand
    sort(potential_cards)
    #print_card_list(potential_cards)
    #print("----------")
    for straight in straights:
        lower = straight[0]
        #print("lower: {0}".format(lower.get_card()))
        upper = straight[-1]
        #print("upper: {0}".format(upper.get_card()))
        lower_outs = {Card.Card(lower.value-1, "Diamonds"), Card.Card(lower.value-1, "Hearts"), Card.Card(lower.value-1, "Spades"), Card.Card(lower.value-1, "Clubs")}
        #print_card_list(lower_outs)
        upper_outs = {Card.Card(upper.value+1, "Diamonds"), Card.Card(upper.value+1, "Hearts"), Card.Card(upper.value+1, "Spades"), Card.Card(upper.value+1, "Clubs")}
        #print_card_list(upper_outs)
        upper_out_status, lower_out_status = True, True
        for card in potential_cards:
            #print(card.get_card())
            if card.value == list(upper_outs)[0].value:
                upper_out_status = False
            if card.value == list(lower_outs)[0].value:
                lower_out_status = False
        #print("upper_out_status: {0}".format(upper_out_status))
        #print("lower_out_status: {0}".format(lower_out_status))
        if upper_out_status and upper.value != 14:
                outs.update(upper_outs)
        if lower_out_status and lower.value != 2:
                outs.update(lower_outs)
        #print("----------")
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
print("----------")

outs = get_straight_outs(straights, in_hand, in_play)
print("Outs")
for card in outs:
    print(card.get_card())
print("----------")