import random, Deck, Card, Hand

class Player():

    #isBigBlind = False
    #isLittleBlind = Flase

    def __init__(self, name):
        self.name = name
        self.hand = Hand.Hand()
        self.stack = 10

    def print_stack_size(self):
        print(self.stack)
    
    def is_stack_empty(self):
        if self.stack == 0:
            return True
        else:
            return False