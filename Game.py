import random, Deck, Card, Hand, Player, Rank

def deal_to_player(player):
    player.hand.add_to_hand(in_deck.deal())

def deal_flop():
    in_discard.append(in_deck.deal())
    for x in range(3):
        in_play.append(in_deck.deal())

def deal_turn():
    in_discard.append(in_deck.deal())
    in_play.append(in_deck.deal())

def deal_river():
    in_discard.append(in_deck.deal())
    in_play.append(in_deck.deal())

player_1 = Player.Player("player_1")
player_2 = Player.Player("player_2")
round = 0

#while ((player_1.is_stack_empty == False) & (player_2.is_stack_empty == False)):
in_deck = Deck.Deck()
in_play = []
in_discard = []
deal_to_player(player_1)
deal_to_player(player_2)
deal_to_player(player_1)
deal_to_player(player_2)
deal_flop()
deal_turn()
deal_river()

print("--------\nIn play\n--------")
for card in in_play:
    print(card.print_card())
print("--------\nPlayer 1\n--------")
player_1.hand.show_hand()
print("--------\nPlayer 2\n--------")
player_2.hand.show_hand()

in_play_rank = Rank.Rank(in_play)
in_play_rank.print_rank()