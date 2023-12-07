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

def print_card_list(card_list):
    card_list = list(card_list)
    if len(card_list) == 4:
        print("{0}, {1}, {2}, {3}".format(card_list[0].get_card(), card_list[1].get_card(), card_list[2].get_card(), card_list[3].get_card()))
    if len(card_list) == 5:
        print("{0}, {1}, {2}, {3}, {4}".format(card_list[0].get_card(), card_list[1].get_card(), card_list[2].get_card(), card_list[3].get_card(), card_list[4].get_card()))

# returns list of 4 card flushes made from possible cards in play and in hand
def get_flushes(in_play, in_hand):
    flushes = []
    potential_cards = in_play + in_hand
    possible_combinations = list(combinations(potential_cards, 4))
    for entry in possible_combinations:
        suit_count = {"Diamonds":0, "Hearts":0, "Spades":0, "Clubs":0}
        for card in entry:
            suit_count[card.suit] += 1
        flush = False
        for key, value in suit_count.items():
            if value == 4:
                flush = True
        if flush:
            flushes.append(entry)
    return flushes

# returns set of cards that are outs
def get_flush_outs(flushes, in_hand, in_play):
    outs = set()
    potential_cards = in_play + in_hand
    for flush in flushes:
        flush_set = set()
        for card in flush:
            flush_set.add(card.value)
        suit_set = set()
        suit = flush[0].suit
        for x in range(2,15):
            suit_set.add(x)
        temp_set = suit_set.difference(flush_set)
        for value in temp_set:
            exists_in_outs = False
            for card in outs:
                if ((card.value == value) and (card.suit == suit)):
                    exists_in_outs = True
            if not exists_in_outs:
                exists_in_potential_cards = False
                for card in potential_cards:
                    if ((card.value == value) and (card.suit == suit)):
                        exists_in_potential_cards = True
                if not exists_in_potential_cards:
                    outs.add(Card.Card(value, suit))
    return outs