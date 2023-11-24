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
        elif current_rank.rank == best_rank.rank:
            if current_rank.rank == 1: # high card
                if current_rank.high_card.value > best_rank.high_card.value:
                    best_rank = current_rank
            elif current_rank.rank == 2: # one pair
                if current_rank.one_pair["value"] > best_rank.one_pair["value"]:
                    best_rank = current_rank
                elif current_rank.one_pair["value"] == best_rank.one_pair["value"]:
                    if current_rank.high_card.value > best_rank.high_card.value:
                        best_rank = current_rank
            elif current_rank.rank == 3: # two pair
                if current_rank.two_pair["high"] > best_rank.two_pair["high"]:
                    best_rank = current_rank
                elif current_rank.two_pair["high"] == best_rank.two_pair["high"]:
                    if current_rank.two_pair["low"] > best_rank.two_pair["low"]:
                        best_rank = current_rank
                    elif current_rank.two_pair["low"] == best_rank.two_pair["low"]:
                        if current_rank.high_card.value > best_rank.high_card.value:
                            best_rank = current_rank
            elif current_rank.rank == 4: # three of a kind
                if current_rank.three_of_a_kind["value"] > best_rank.three_of_a_kind["value"]:
                    best_rank = current_rank
                elif current_rank.three_of_a_kind["value"] == best_rank.three_of_a_kind["value"]:
                    if current_rank.high_card.value > best_rank.high_card.value:
                        best_rank = current_rank
            elif current_rank.rank == 5: # straight
                if current_rank.straight["high"] > best_rank.straight["high"]:
                    best_rank = current_rank
                elif current_rank.straight["high"] == best_rank.straight["high"]:
                    if current_rank.high_card.value > best_rank.high_card.value:
                        best_rank = current_rank
            elif current_rank.rank == 6: # flush
                if current_rank.card_list[-1] > best_rank.card_list[-1]:
                    best_rank = current_rank
                elif current_rank.card_list[-1] == best_rank.card_list[-1]:
                    if current_rank.card_list[-2] > best_rank.card_list[-2]:
                        best_rank = current_rank
                    elif current_rank.card_list[-2] == best_rank.card_list[-2]:
                        if current_rank.card_list[-3] > best_rank.card_list[-3]:
                            best_rank = current_rank
                        elif current_rank.card_list[-3] == best_rank.card_list[-3]:
                            if current_rank.card_list[-4] > best_rank.card_list[-4]:
                                best_rank = current_rank
                            elif current_rank.card_list[-4] == best_rank.card_list[-4]:
                                if current_rank.card_list[-5] > best_rank.card_list[-5]:
                                    best_rank = current_rank
            elif current_rank.rank == 7: # full house
                if current_rank.full_house["three_of_a_kind_value"] > best_rank.full_house["three_of_a_kind_value"]:
                    best_rank = current_rank
                elif current_rank.full_house["three_of_a_kind_value"] == best_rank.full_house["three_of_a_kind_value"]:
                    if current_rank.full_house["one_pair_value"] > best_rank.full_house["one_pair_value"]:
                        best_rank = current_rank
            elif current_rank.rank == 8: # four of a kind
                if current_rank.four_of_a_kind["value"] > best_rank.four_of_a_kind["value"]:
                    best_rank = current_rank
                elif current_rank.four_of_a_kind["value"] == best_rank.four_of_a_kind["value"]:
                    if current_rank.high_card.value > best_rank.high_card.value:
                        best_rank = current_rank
            elif current_rank.rank == 9: # straight flush
                if current_rank.straight_flush["high"] > best_rank.straight_flush["high"]:
                    best_rank = current_rank
            # no royal flush tie possible
    return best_rank

def compare(p1_value, p2_value):
    if p1_value > p2_value:
        return "p1"
    elif p2_value > p1_value:
        return "p2"
    else:
        return "tie"

# somewhat duplicate from hand ranking code, will optimize in the future
def compare_player_hands(p1_best_rank, p2_best_rank):
    winner = ""
    if p1_best_rank.rank == 1: # high card
        winner = compare(p1_best_rank.high_card, p2_best_rank.high_card)
    elif p1_best_rank.rank.rank == 2: # one pair
        winner = compare(p1_best_rank.one_pair["value"], p2_best_rank.one_pair["value"])
        if winner == "tie":
            winner = compare(p1_best_rank.high_card, p2_best_rank.high_card)
    elif p1_best_rank.rank == 3: # two pair
        winner = compare(p1_best_rank.two_pair["high"], p2_best_rank.two_pair["high"])
        if winner == "tie":
            winner = compare(p1_best_rank.two_pair["low"], p2_best_rank.two_pair["low"])
            if winner == "tie":
                winner = compare(p1_best_rank.high_card, p2_best_rank.high_card)
    elif p1_best_rank.rank == 4: # three of a kind
        winner = compare(p1_best_rank.three_of_a_kind["value"], p2_best_rank.three_of_a_kind["value"])
        if winner == "tie":
            winner = compare(p1_best_rank.high_card, p2_best_rank.high_card)
    elif p1_best_rank.rank == 5: # straight
        winner = compare(p1_best_rank.straight["high"], p2_best_rank.straight["high"])
        if winner == "tie":
            winner = compare(p1_best_rank.high_card, p2_best_rank.high_card)
    elif p1_best_rank.rank == 6: # flush
        winner = compare(p1_best_rank.card_list[-1], p2_best_rank.card_list[-1])
        if winner == "tie":
            winner = compare(p1_best_rank.card_list[-2], p2_best_rank.card_list[-2])
            if winner == "tie":
                winner = compare(p1_best_rank.card_list[-3], p2_best_rank.card_list[-3])
                if winner == "tie":
                    winner = compare(p1_best_rank.card_list[-4], p2_best_rank.card_list[-4])
                    if winner == "tie":
                        winner = compare(p1_best_rank.card_list[-5], p2_best_rank.card_list[-5])
    elif p1_best_rank.rank == 7: # full house
        winner = compare(p1_best_rank.full_house["three_of_a_kind_value"], p2_best_rank.full_house["three_of_a_kind_value"])
        if winner == "tie":
            winner = compare(p1_best_rank.full_house["one_pair_value"], p2_best_rank.full_house["one_pair_value"])
    elif p1_best_rank.rank == 8: # four of a kind
        winner = compare(p1_best_rank.four_of_a_kind["value"], p2_best_rank.four_of_a_kind["value"])
        if winner == "tie":
            winner = compare(p1_best_rank.high_card, p2_best_rank.high_card)
    elif p1_best_rank.rank == 9: # straight flush
        winner = compare(p1_best_rank.straight_flush["high"], p2_best_rank.straight_flush["high"])
    # no royal flush tie possible
    return winner


def get_card_list(card_objects_list):
    card_list = []
    for card in card_objects_list:
        card_list.append(card.get_card())
    return card_list


if __name__ == '__main__':

    # start timer for program execution
    start_time = time.time()

    player_1 = Player.Player("player")
    player_1.swap_button()
    button = 1
    player_2 = Player.Player("AI")
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
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p1.hand.in_hand), p1.stack, p1.name))
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p2.hand.in_hand), p2.stack, p2.name))

        # intial betting
        # betting loop
        p1_bet, p2_bet = -1, -1
        while p1_bet < 0:
            bet = input("How much will you bet?")
            if bet == '':
                bet = 0
            else:
                bet = int(bet)
            if p1.can_bet(bet):
                p1_bet = bet
                pot += p1.bet(p1_bet)
        while p2_bet < 0:
            #bet = input("How much will you bet?")
            #if bet == '':
            #    bet = 0
            #else:
            #    bet = int(bet)
            bet = p1_bet # p2 is always calling for now until AI is implemented
            if p2.can_bet(bet):
                p2_bet = bet
                pot += p2.bet(p2_bet)
                print("AI calls {0}".format(bet))
        print("Total pot: {0}".format(pot))

        # FLOP STAGE
        print("---------------\nStage: Flop")
        # show player hole cards
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p1.hand.in_hand), p1.stack, p1.name))
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p2.hand.in_hand), p2.stack, p2.name))
        deal_flop()
        print("In play: {0}".format(get_card_list(in_play)))

        # betting loop
        p1_bet, p2_bet = -1, -1
        while p1_bet < 0:
            bet = input("How much will you bet?")
            if bet == '':
                bet = 0
            else:
                bet = int(bet)
            if p1.can_bet(bet):
                p1_bet = bet
                pot += p1.bet(p1_bet)
        while p2_bet < 0:
            #bet = input("How much will you bet?")
            #if bet == '':
            #    bet = 0
            #else:
            #    bet = int(bet)
            bet = p1_bet # p2 is always calling for now until AI is implemented
            if p2.can_bet(bet):
                p2_bet = bet
                pot += p2.bet(p2_bet)
                print("AI calls {0}".format(bet))
        print("Total pot: {0}".format(pot))

        # TURN STAGE
        print("---------------\nStage: Turn")
        # show player hole cards
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p1.hand.in_hand), p1.stack, p1.name))
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p2.hand.in_hand), p2.stack, p2.name))
        deal_turn()
        print("In play: {0}".format(get_card_list(in_play)))

        # betting loop
        p1_bet, p2_bet = -1, -1
        while p1_bet < 0:
            bet = input("How much will you bet?")
            if bet == '':
                bet = 0
            else:
                bet = int(bet)
            if p1.can_bet(bet):
                p1_bet = bet
                pot += p1.bet(p1_bet)
        while p2_bet < 0:
            #bet = input("How much will you bet?")
            #if bet == '':
            #    bet = 0
            #else:
            #    bet = int(bet)
            bet = p1_bet # p2 is always calling for now until AI is implemented
            if p2.can_bet(bet):
                p2_bet = bet
                pot += p2.bet(p2_bet)
                print("AI calls {0}".format(bet))
        print("Total pot: {0}".format(pot))

        # RIVER STAGE
        print("---------------\nStage: River")
        # show player hole cards
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p1.hand.in_hand), p1.stack, p1.name))
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p2.hand.in_hand), p2.stack, p2.name))
        deal_river()
        print("In play: {0}".format(get_card_list(in_play)))

        # betting loop
        p1_bet, p2_bet = -1, -1
        while p1_bet < 0:
            bet = input("How much will you bet?")
            if bet == '':
                bet = 0
            else:
                bet = int(bet)
            if p1.can_bet(bet):
                p1_bet = bet
                pot += p1.bet(p1_bet)
        while p2_bet < 0:
            #bet = input("How much will you bet?")
            #if bet == '':
            #    bet = 0
            #else:
            #    bet = int(bet)
            bet = p1_bet # p2 is always calling for now until AI is implemented
            if p2.can_bet(bet):
                p2_bet = bet
                pot += p2.bet(p2_bet)
                print("AI calls {0}".format(bet))
        print("Total pot: {0}".format(pot))

        p1_best_rank = rank_player_possible_hands(p1, in_play)
        print("---------------\n{2} Rank: {0}\nBest Hand: {1}".format(
            p1_best_rank.get_rank(), p1_best_rank.description, p1.name))
        #print("value_count: {0}".format(p1_best_rank.value_count))
        #print("suit_count: {0}".format(p1_best_rank.suit_count))
        print(get_card_list(p1_best_rank.card_list))

        p2_best_rank = rank_player_possible_hands(p2, in_play)
        print("---------------\n{2} Rank: {0}\nBest Hand: {1}".format(
            p2_best_rank.get_rank(), p2_best_rank.description, p2.name))
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
                print("\n{0} Wins\n".format(p1.name))
            elif p2_best_rank.rank > p1_best_rank.rank:
                p2.stack += pot
                print("\n{0} Wins\n".format(p2.name))
            else:
                winner = compare_player_hands(p1_best_rank, p2_best_rank)
                if winner == "p1":
                    p1.stack += pot
                    print("\n{0} Wins\n".format(p1.name))
                elif winner == "p2":
                    p2.stack += pot
                    print("\n{0} Wins\n".format(p2.name))
                else:
                    p1.stack += pot/2
                    p2.stack += pot/2
                    print("\nDraw\n")

        print("{1} Stack Size: {0}".format(p1.stack, p1.name))
        print("{1} Stack Size: {0}\n\n".format(p2.stack, p2.name))
        p1.clear_hand()
        p2.clear_hand()
        p1.swap_button()
        p2.swap_button()
        button = 1 if button == 2 else 2
        round += 1
    
    print("{1} Stack Size: {0}".format(p1.stack, p1.name))
    print("{1} Stack Size: {0}\n\n".format(p2.stack, p2.name))
    if p1.stack > p2.stack:
        print("---------------\nPlayer 1 wins!")
    else:
        print("---------------\nPlayer 2 wins!")

    # end timer
    print("--- Execution Time: {0} ---".format(
        datetime.timedelta(seconds=(time.time() - start_time))))
