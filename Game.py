import time
import datetime
import random
import Deck
import Card
import Hand
import Player
from Rank import Rank
from itertools import combinations


def can_play(player):
    return not player.is_stack_empty()


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

    # start timer for program execution
    start_time = time.time()

    player_1 = Player.Player("player_1")
    player_1.swap_button()
    button = 1
    player_2 = Player.Player("player_2")
    round = 0

    while (can_play(player_1) & can_play(player_2)):
        pot = 0
        in_deck = Deck.Deck()
        in_play = []
        in_discard = []

        print("\nRound: [{0}]".format(round))

        # Set player order
        p1 = player_1 if player_1.is_button() else player_2
        p2 = player_1 if p1 == player_2 else player_2

        # PREFLOP STAGE
        print("---------------\nStage: Preflop")
        deal_to_player(p1)
        deal_to_player(p2)
        deal_to_player(p1)
        deal_to_player(p2)

        # show player hole cards
        print("Player {2} Hole Cards: {0},   Stack Size: {1}".format(
            get_card_list(p1.hand.in_hand), p1.stack, button))
        print("Player {2} Hole Cards: {0},   Stack Size: {1}".format(
            get_card_list(p2.hand.in_hand), p2.stack, 1 if button == 2 else 2))

        # intial betting
        bet = int(input("How much will you bet?"))
        pot += p1.bet(bet)
        # p2 is always calling for now until AI is implemented
        print("Player 2 calls {0}".format(bet))
        pot += p2.bet(bet)
        print("Total pot: {0}".format(pot))

        # FLOP STAGE
        print("---------------\nStage: Flop")
        # show player hole cards
        print("Player {2} Hole Cards: {0},   Stack Size: {1}".format(
            get_card_list(p1.hand.in_hand), p1.stack, button))
        print("Player {2} Hole Cards: {0},   Stack Size: {1}".format(
            get_card_list(p2.hand.in_hand), p2.stack, 1 if button == 2 else 2))
        deal_flop()
        print("In play: {0}".format(get_card_list(in_play)))

        bet = int(input("How much will you bet?"))
        pot += p1.bet(bet)
        # p2 is always calling for now until AI is implemented
        print("Player 2 calls {0}".format(bet))
        pot += p2.bet(bet)
        print("Total pot: {0}\n".format(pot))

        # TURN STAGE
        print("---------------\nStage: Turn")
        # show player hole cards
        print("Player {2} Hole Cards: {0},   Stack Size: {1}".format(
            get_card_list(p1.hand.in_hand), p1.stack, button))
        print("Player {2} Hole Cards: {0},   Stack Size: {1}".format(
            get_card_list(p2.hand.in_hand), p2.stack, 1 if button == 2 else 2))
        deal_turn()
        print("In play: {0}".format(get_card_list(in_play)))

        bet = int(input("How much will you bet?"))
        pot += p1.bet(bet)
        # p2 is always calling for now until AI is implemented
        print("Player 2 calls {0}".format(bet))
        pot += p2.bet(bet)
        print("Total pot: {0}\n".format(pot))

        # RIVER STAGE
        print("---------------\nStage: River")
        # show player hole cards
        print("Player {2} Hole Cards: {0},   Stack Size: {1}".format(
            get_card_list(p1.hand.in_hand), p1.stack, button))
        print("Player {2} Hole Cards: {0},   Stack Size: {1}".format(
            get_card_list(p2.hand.in_hand), p2.stack, 1 if button == 2 else 2))
        deal_river()
        print("In play: {0}".format(get_card_list(in_play)))

        bet = int(input("How much will you bet?"))
        pot += p1.bet(bet)
        # p2 is always calling for now until AI is implemented
        print("Player 2 calls {0}".format(bet))
        pot += p2.bet(bet)
        print("Total pot: {0}\n".format(pot))

        p1_best_rank = rank_player_possible_hands(p1, in_play)
        print("---------------\nPlayer 1 Rank: {0}\nBest Hand: {1}".format(
            p1_best_rank.get_rank(), p1_best_rank.description))
        #print("value_count: {0}".format(p1_best_rank.value_count))
        #print("suit_count: {0}".format(p1_best_rank.suit_count))
        print(get_card_list(p1_best_rank.card_list))

        p2_best_rank = rank_player_possible_hands(p2, in_play)
        print("---------------\nPlayer 2 Rank: {0}\nBest Hand: {1}".format(
            p2_best_rank.get_rank(), p2_best_rank.description))
        #print("value_count: {0}".format(p2_best_rank.value_count))
        #print("suit_count: {0}".format(p2_best_rank.suit_count))
        print(get_card_list(p2_best_rank.card_list))

        if p1_best_rank.card_list == p2_best_rank.card_list:
            p1.stack += pot/2
            p2.stack += pot/2
            print("\nDraw\n")
        else:
            if p1_best_rank.rank > p2_best_rank.rank:
                p1.stack += pot
                print("\nPlayer 1 Wins\n")
            elif p2_best_rank.rank > p1_best_rank.rank:
                p2.stack += pot
                print("\nPlayer 2 Wins\n")
            else:
                if p1_best_rank.high_card.value > p2_best_rank.high_card.value:
                    p1.stack += pot
                    print("\nPlayer 1 Wins\n")
                elif p2_best_rank.high_card.value > p1_best_rank.high_card.value:
                    p2.stack += pot
                    print("\nPlayer 2 Wins\n")
                else:
                    p1.stack += pot/2
                    p2.stack += pot/2
                    print("\nDraw\n")

        print("Player 1 Stack Size: {0}".format(p1.stack))
        print("Player 2 Stack Size: {0}\n\n".format(p2.stack))
        p1.clear_hand()
        p2.clear_hand()
        p1.swap_button()
        p2.swap_button()
        button = 1 if button == 2 else 2
        round += 1

    # end timer
    print("--- Execution Time: {0} ---".format(
        datetime.timedelta(seconds=(time.time() - start_time))))
