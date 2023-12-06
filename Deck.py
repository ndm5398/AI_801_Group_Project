import random, Card

class Deck:

    def __init__(self):
        self.in_deck = []
        self.construct()
        self.shuffle_deck()
    
    def construct(self):
        for suit in ["Diamonds", "Hearts", "Spades", "Clubs"]:
            for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
                self.in_deck.append(Card.Card(value, suit))
    
    def print_deck(self):
        for c in self.in_deck:
            c.print_card()
    
    def shuffle_deck(self):
        random.shuffle(self.in_deck)

    def deal(self):
        c = self.in_deck.pop()
        return c