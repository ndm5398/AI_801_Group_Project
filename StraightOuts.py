import Card
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

# returns set of cards that are outs
def get_straight_outs(straights, in_hand, in_play):
    outs = set()
    potential_cards = in_play + in_hand
    sort(potential_cards)
    for straight in straights:
        lower = straight[0]
        upper = straight[-1]
        lower_outs = {Card.Card(lower.value-1, "Diamonds"), Card.Card(lower.value-1, "Hearts"), Card.Card(lower.value-1, "Spades"), Card.Card(lower.value-1, "Clubs")}
        upper_outs = {Card.Card(upper.value+1, "Diamonds"), Card.Card(upper.value+1, "Hearts"), Card.Card(upper.value+1, "Spades"), Card.Card(upper.value+1, "Clubs")}
        upper_out_status, lower_out_status = True, True
        for card in potential_cards:
            if card.value == list(upper_outs)[0].value:
                upper_out_status = False
            if card.value == list(lower_outs)[0].value:
                lower_out_status = False
        if upper_out_status and upper.value != 14:
            outs.update(upper_outs)
        if lower_out_status and lower.value != 2:
            outs.update(lower_outs)
        elif lower_out_status and lower.value == 2:
            lower_outs = {Card.Card(14, "Diamonds"), Card.Card(14, "Hearts"), Card.Card(14, "Spades"), Card.Card(14, "Clubs")}
            outs.update(lower_outs)
    return outs