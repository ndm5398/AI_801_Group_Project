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
        self.stack = 10
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

    def bet(self, value):
        if self.is_stack_empty():
            print("Can not bet anymore, you are all in")
        else:
            if (self.stack - value) < 0:
                print("Not enough chips to bet {1}, you are all in".format(
                    self.name, value))
                self.stack = 0
                return self.stack
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
