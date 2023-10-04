class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        if self.value == 11:
            self.name = "Jack"
        elif self.value == 12:
            self.name = "Queen"
        elif self.value == 13:
            self.name = "King"
        elif self.value == 14:
            self.name = "Ace"
        else:
            self.name = self.value
        
    
    def get_card(self):
        return "{0} of {1}".format(self.name, self.suit)