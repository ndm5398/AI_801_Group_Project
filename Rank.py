import Card

class Rank:

    def __init__(self, cards):
        self.rank = 0
        self.description = ""
        self.suit_count = {"Diamonds":0, "Hearts":0, "Spades":0, "Clubs":0}
        self.value_count = {"2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0}
        self.card_list = cards
        self.sort_cards()
        for card in self.card_list:
            self.suit_count[card.suit] += 1
            self.value_count[str(card.value)] += 1
        self.high_card = self.card_list[-1]
        self.one_pair, self.two_pair, self.three_of_a_kind, self.straight, self.flush, self.full_house, self.four_of_a_kind, self.straight_flush, self.royal_flush = {}, {}, {}, {}, {}, {}, {}, {}, {}
        self.is_one_pair()
        self.is_two_pair()
        self.is_three_of_a_kind()
        self.is_straight()
        self.is_flush()
        self.is_full_house() 
        self.is_four_of_a_kind()
        self.is_straight_flush()
        self.is_royal_flush()
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
        
    def is_one_pair(self):
        count = 0
        temp = ""
        for key, value in self.value_count.items():
            if value == 2:
                count += 1
                temp = key
        if count == 1:
            self.one_pair["value"] = temp   

    def is_two_pair(self):
        count = 0
        temp = []
        for key, value in self.value_count.items():
            if value == 2:
                count += 1
                temp.append(int(key))
        if count == 2:
            temp.sort()
            self.two_pair["low"] = temp[0]
            self.two_pair["high"] = temp[1]

    def is_three_of_a_kind(self):
        for key, value in self.value_count.items():
            if value == 3:
                self.three_of_a_kind["value"] = key

    def is_straight(self):
        test = True
        for x in range(len(self.card_list)-1):
            if self.card_list[x].value + 1 != self.card_list[x+1].value:
                test = False
        if test:
            self.straight["high"] = self.card_list[-1]

    def is_flush(self):
        for key, value in self.suit_count.items():
            if value == 5:
                self.flush["suit"] = key

    def is_full_house(self):
        if (self.one_pair and self.three_of_a_kind):
            self.full_house["one_pair_value"] = self.one_pair["value"]
            self.full_house["three_of_a_kind_value"] = self.three_of_a_kind["value"]

    def is_four_of_a_kind(self):
        for key, value in self.value_count.items():
            if value == 4:
                self.four_of_a_kind["value"] = key
            
    def is_straight_flush(self):
        if (self.straight and self.flush):
            self.straight_flush["straight_high"] = self.straight["high"]
            self.straight_flush["flush_suit"] = self.flush["suit"]

    def is_royal_flush(self):
        if ((self.card_list[0].value == 10) and self.straight and self.flush):
            self.royal_flush["straight_high"] = self.straight["high"]
            self.royal_flush["flush_suit"] = self.flush["suit"]
        
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
        




