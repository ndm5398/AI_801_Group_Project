import time, datetime, random, Deck, Card, Hand, Player
from Rank import Rank
from itertools import combinations

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

def rank_player_possible_hands(player, cards_in_play):
    potential_cards = cards_in_play + player.hand.in_hand
    possible_combinations = list(combinations(potential_cards, 5))
    best_rank = Rank(list(possible_combinations[0]))
    for entry in possible_combinations:
        current_rank = Rank(list(entry))
        if current_rank.rank > best_rank.rank:
            best_rank = current_rank
    return best_rank

def get_card_list(card_objects_list):
    card_list = []
    for card in card_objects_list:
        card_list.append(card.get_card())
    return card_list


if __name__ == '__main__':

    #start timer for program execution
    start_time = time.time()

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


    print("\nIn play\n--------")
    print(get_card_list(in_play))
    print("--------\nPlayer 1 Hole Cards\n--------")
    print(get_card_list(player_1.hand.in_hand))
    print("--------\nPlayer 2 Hole Cards\n--------")
    print(get_card_list(player_2.hand.in_hand))

    player_1_best_rank = rank_player_possible_hands(player_1, in_play)
    print("--------\nPlayer 1 Rank: {0}\nBest Hand: {1}".format(player_1_best_rank.get_rank(), player_1_best_rank.description))
    #print("value_count: {0}".format(player_1_best_rank.value_count))
    #print("suit_count: {0}".format(player_1_best_rank.suit_count))
    print(get_card_list(player_1_best_rank.card_list))

    
    player_2_best_rank = rank_player_possible_hands(player_2, in_play)
    print("--------\nPlayer 2 Rank: {0}\nBest Hand: {1}".format(player_2_best_rank.get_rank(), player_2_best_rank.description))
    #print("value_count: {0}".format(player_2_best_rank.value_count))
    #print("suit_count: {0}".format(player_2_best_rank.suit_count))
    print(get_card_list(player_2_best_rank.card_list))

    if player_1_best_rank.card_list == player_2_best_rank.card_list:
        print("\nDraw\n")
    else:
        if player_1_best_rank.rank > player_2_best_rank.rank:
            print("\nPlayer 1 Wins\n")
        elif player_2_best_rank.rank > player_1_best_rank.rank:
            print("\nPlayer 2 Wins\n")
        else:
            if player_1_best_rank.high_card.value > player_2_best_rank.high_card.value:
                print("\nPlayer 1 Wins\n")
            elif player_2_best_rank.high_card.value > player_1_best_rank.high_card.value:
                print("\nPlayer 2 Wins\n")
            else:
                print("\nDraw\n")


    #end timer
    print("--- Execution Time: {0} ---".format(datetime.timedelta(seconds=(time.time() - start_time))))