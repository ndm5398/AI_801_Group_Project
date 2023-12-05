import random
import Deck
import Card
import Hand


class Player():

    #isBigBlind = False
    #isLittleBlind = Flase

    def __init__(self, name):
        self.name = name
        self.hand = Hand.Hand()
        self.stack = 100
        self.button = False

    def is_stack_empty(self):
        if self.stack == 0:
            return True
        else:
            return False

    def is_button(self):
        return self.button

    def swap_button(self):
        self.button = not self.button

    def can_bet(self, value):
        if (self.is_stack_empty() and (value > 0)):
            print("ERROR: {0} stack is empty".format(self.name))
            return False
        elif (self.stack - value) < 0:
            print("ERROR: {0} Not enough chips to bet {1}".format(self.name, value))
            return False
        else:
            return True

    def bet(self, value):
        if self.can_bet(value):
            self.stack -= value
            return value
        else:
            self.stack = 0
            return self.stack

    def bet_all_in(self):
        if self.is_stack_empty():
            print("ERROR: {0} stack is empty".format(self.name))
        else:
            all_in = self.stack
            self.stack = 0
            return all_in

    def clear_hand(self):
        self.hand = Hand.Hand()
