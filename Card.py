class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def print_card(self):
        if self.value == 11:
            name = "Jack"
        elif self.value == 12:
            name = "Queen"
        elif self.value == 13:
            name = "King"
        elif self.value == 14:
            name = "Ace"
        else:
            name = self.value
        return "{0} of {1}".format(name, self.suit)