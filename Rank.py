import Card

class Rank:

    description = ""
    high_card = ""
    rank = 0
    suit_count = {"Diamonds":0, "Hearts":0, "Spades":0, "Clubs":0}
    value_count = {"2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0}

    def __init__(self, cards):
        self.card_list = cards
        self.sort_cards()
        for card in self.card_list:
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
    
    def sort_cards(self):
        for x in range((len(self.card_list))):
            for y in range (x+1, (len(self.card_list)), 1):
                if self.card_list[x].value > self.card_list[y].value:
                    swap = self.card_list[x]
                    self.card_list[x] = self.card_list[y]
                    self.card_list[y] = swap

    def get_rank(self):
        return self.rank
    
    def print_rank(self):
        print("Rank = {0}".format(self.rank))

    def high_card(self):
        self.high_card = self.card_list[-1].get_card()
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

    def is_straight(self):
        for x in range(len(self.card_list)-1):
            if self.card_list[x].value + 1 != self.card_list[x+1].value:
                return False
        return True

    def is_flush(self):
        for key, value in self.suit_count.items():
            if value == 5:
                return True
        return False

    def is_full_house(self):
        return (self.is_one_pair() & self.is_three_of_a_kind())

    def is_four_of_a_kind(self):
        for key, value in self.value_count.items():
            if value == 4:
                return True
        return False
            
    def is_straight_flush(self):
        return (self.is_straight() & self.is_flush())

    def is_royal_flush(self):
        if ((self.card_list[0].value == 10) & self.is_straight() & self.is_flush()):
            return True
        else:
            return False
        
    def rank_hand(self):
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
        




