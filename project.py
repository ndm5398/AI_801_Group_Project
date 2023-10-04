import Deck, Card, Hand

hand = Hand.Hand()
suit_count = {
    "Diamonds" : 0,
    "Hearts" : 0,
    "Spades" : 0,
    "Clubs" : 0
}
value_count = {
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0,
    "6" : 0,
    "7" : 0,
    "8" : 0,
    "9" : 0,
    "10" : 0,
    "11" : 0,
    "12" : 0,
    "13" : 0,
    "14" : 0
}

deck = Deck.Deck()

for x in range(5):
    hand.add_to_hand(deck.deal())


for card in hand.in_hand:
    suit_count[card.suit] += 1
    value_count[str(card.value)] += 1
    card.print_card()


def high_card(hand):
    hand.sort_hand()
    return hand.in_hand[-1]


def is_pair(dict):
    count = 0
    for key, value in dict.items():
        if value == 2:
            count += 1
    if count == 1:
        return True
    else:
        return False
        

def is_two_pair(dict):
    count = 0
    for key, value in dict.items():
        if value == 2:
            count += 1
    if count == 2:
        return True
    else:
        return False
    

def is_three_of_a_kind(dict):
    for key, value in dict.items():
        if value == 3:
            return True
    return False
        

def is_straight(hand):
    hand.sort_hand()
    for x in range(len(hand.in_hand)-1):
        if hand.in_hand[x].value + 1 != hand.in_hand[x+1].value:
            return False
    return True


def is_flush(dict):
    for key, value in dict.items():
        if value == 5:
            return True
    return False
        

def is_full_house(dict):
    return (is_pair(dict) & is_three_of_a_kind(dict))


def is_four_of_a_kind(dict):
    for key, value in dict.items():
        if value == 4:
            return True
    return False
        

def is_straight_flush(hand, suit_dict):
    return (is_straight(hand) & is_flush(suit_dict))


def is_royal_flush(hand, suit_dict):
    hand.sort_hand()
    if ((hand.in_hand[0].value == 10) & is_straight(hand) & is_flush(suit_dict)):
        return True
    else:
        return False

print()
print(suit_count)
print()
print(value_count)
print()
print("High Card? : {0}".format(high_card(hand).print_card()))
print("Pair? {0}".format(is_pair(value_count)))
print("Two Pair? {0}".format(is_two_pair(value_count)))
print("Three of a Kind? {0}".format(is_three_of_a_kind(value_count)))
print("Straight? {0}".format(is_straight(hand)))
print("Flush? {0}".format(is_flush(suit_count)))
print("Full House? {0}".format(is_full_house(value_count)))
print("Four of a Kind? {0}".format(is_four_of_a_kind(value_count)))
print("Straight Flush? {0}".format(is_straight_flush(hand, suit_count)))
print("Royal Flush? {0}".format(is_royal_flush(hand, suit_count)))