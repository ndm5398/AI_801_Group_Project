
class Hand:

    def __init__(self):
        self.in_hand = []

    def add_to_hand(self, card):
        self.in_hand.append(card)

    def sort_hand(self):
        for x in range((len(self.in_hand))):
            for y in range(x+1, (len(self.in_hand)), 1):
                if self.in_hand[x].value > self.in_hand[y].value:
                    swap = self.in_hand[x]
                    self.in_hand[x] = self.in_hand[y]
                    self.in_hand[y] = swap

    def show_hand(self):
        for c in self.in_hand:
            print(c.get_card())

    def is_suited(self):
        return self.in_hand[0].suit == self.in_hand[1].suit

    def is_connected(self):
        return abs(self.in_hand[0].value - self.in_hand[1].value) == 1

    def is_broadway(self):
        return self.in_hand[0].value > 10 and self.in_hand[1].value > 10
