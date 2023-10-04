import random, Hand, Deck


class Round:

    in_deck = Deck.Deck()
    in_play = []
    in_discard = []  
    
    def __init__(self, number, player_1, player_2):
        self.number = number
        self.player_1 = player_1
        self.player_2 = player_2
        
    


            self.in_play.append(c)