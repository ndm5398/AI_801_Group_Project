import Card, Hand

class Rank:

    description = ""
    high_card = ""
    rank = 0
    suit_count = {"Diamonds":0, "Hearts":0, "Spades":0, "Clubs":0}
    value_count = {"2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0}
    pair = False
    two_pair = False
    three_of_a_kind = False
    straight = False
    flush = False
    full_house = False
    four_of_a_kind = False
    straight_flush = False
    royal_flush = False

    def __init__(self, hand):
        for card in hand.in_hand:
            self.suit_count[card.suit] += 1
            self.value_count[str(card.value)] += 1
        self.high_card()
        self.one_pair = self.is_one_pair()
        self.two_pair = self.is_two_pair()
        self.three_of_a_kind = self.is_three_of_a_kind()
        self.straight = self.is_straight()
        self.flush = self.is_flush()
        self.full_house = self.is_full_house() 
        self.four_of_a_kind = self.is_four_of_a_kind()
        self.straight_flush = self.is_straight_flush()
        self.royal_flush = self.is_royal_flush()
        self.rank_hand()
        return

    def high_card(self, hand):
        hand.sort_hand()
        self.high_card = hand.in_hand[-1].print_card()
        self.description = self.high_card
        self.rank = 1
        return 

    def is_one_pair(self):
        count = 0
        for key, value in self.value_count.items():
            if value == 2:
                count += 1
        if count == 1:
            return True
        else:
            return False    

    def is_two_pair(self):
        count = 0
        for key, value in self.value_count.items():
            if value == 2:
                count += 1
        if count == 2:
            return True
        else:
            return False 

    def is_three_of_a_kind(self):
        for key, value in self.value_count.items():
            if value == 3:
                return True
        return False 

    def is_straight(self, hand):
        hand.sort_hand()
        for x in range(len(hand.in_hand)-1):
            if hand.in_hand[x].value + 1 != hand.in_hand[x+1].value:
                return False
        return True

    def is_flush(self):
        for key, value in self.suit_count.items():
            if value == 5:
                return True
        return False

    def is_full_house(self):
        return (self.is_pair() & self.is_three_of_a_kind())

    def is_four_of_a_kind(self):
        for key, value in self.value_count.items():
            if value == 4:
                return True
        return False
            
    def is_straight_flush(self, hand):
        return (self.is_straight(hand) & self.is_flush())

    def is_royal_flush(self, hand):
        hand.sort_hand()
        if ((hand.in_hand[0].value == 10) & self.is_straight(hand) & self.is_flush()):
            return True
        else:
            return False
        
    def rank_hand(self, hand):
        if self.royal_flush:
            self.rank = 10
            self.description = "Royal Flush"
            return
        elif self.straight_flush:
            self.rank = 9
            self.description = "Straight Flush"
            return
        elif self.four_of_a_kind:
            self.rank = 8
            self.description = "Four of a Kind"
            return
        elif self.full_house:
            self.rank = 7
            self.description = "Full House"
            return
        elif self.flush:
            self.rank = 6
            self.description = "Flush"
            return
        elif self.straight:
            self.rank = 5
            self.description = "Straight"
            return
        elif self.three_of_a_kind:
            self.rank = 4
            self.description = "Three of a Kind"
            return
        elif self.two_pair:
            self.rank = 3
            self.description = "Two Pair"
            return
        elif self.one_pair:
            self.rank = 2
            self.description = "One Pair"
            return
        else:
            self.rank = 1
            self.description = "High Card"
            return
        




