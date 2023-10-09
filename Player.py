import random, Deck, Card, Hand

class Player():

    #isBigBlind = False
    #isLittleBlind = Flase

    def __init__(self, name):
        self.name = name
        self.hand = Hand.Hand()
        self.stack = 10
    
    def is_stack_empty(self):
        if self.stack == 0:
            return True
        else:
            return False
    
    def bet(self, value):
        if self.is_stack_empty():
            print("ERROR: {0} stack is empty".format(self.name))
        else:
            if (self.stack - value) < 0:
                print("ERROR: {0} Not enough chips to bet {1}".format(self.name, value))
            else:
                self.stack -= value
                return value
    
    def bet_all_in(self):
        if self.is_stack_empty():
            print("ERROR: {0} stack is empty".format(self.name))
        else:
            all_in = self.stack
            self.stack = 0
            return all_in
    
    def clear_hand(self):
        self.hand = Hand.Hand()
