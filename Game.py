import time
import datetime
import random
import Deck
import Card
import Hand
import Player
import Agent
from Rank import Rank
from itertools import combinations
import math


def can_play(player):
    return not player.is_stack_empty()


def deal_to_player(player):
    player.hand.add_to_hand(in_deck.deal())


def deal_flop():
    in_discard.append(in_deck.deal())
    for x in range(3):
        in_play.append(in_deck.deal())
    print("In play: {0}\n".format(get_card_list(in_play)))
    time.sleep(1)



def deal_turn():
    in_discard.append(in_deck.deal())
    in_play.append(in_deck.deal())
    print("In play: {0}\n".format(get_card_list(in_play)))
    time.sleep(1)



def deal_river():
    in_discard.append(in_deck.deal())
    in_play.append(in_deck.deal())
    print("In play: {0}\n".format(get_card_list(in_play)))
    time.sleep(1)



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
        winner = compare(p1_best_rank.high_card.value, p2_best_rank.high_card.value)
    elif p1_best_rank.rank == 2: # one pair
        winner = compare(p1_best_rank.one_pair["value"], p2_best_rank.one_pair["value"])
        if winner == "tie":
            winner = compare(p1_best_rank.high_card.value, p2_best_rank.high_card.value)
    elif p1_best_rank.rank == 3: # two pair
        winner = compare(p1_best_rank.two_pair["high"], p2_best_rank.two_pair["high"])
        if winner == "tie":
            winner = compare(p1_best_rank.two_pair["low"], p2_best_rank.two_pair["low"])
            if winner == "tie":
                winner = compare(p1_best_rank.high_card.value, p2_best_rank.high_card.value)
    elif p1_best_rank.rank == 4: # three of a kind
        winner = compare(p1_best_rank.three_of_a_kind["value"], p2_best_rank.three_of_a_kind["value"])
        if winner == "tie":
            winner = compare(p1_best_rank.high_card.value, p2_best_rank.high_card.value)
    elif p1_best_rank.rank == 5: # straight
        winner = compare(p1_best_rank.straight["high"], p2_best_rank.straight["high"])
        if winner == "tie":
            winner = compare(p1_best_rank.high_card.value, p2_best_rank.high_card.value)
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
            winner = compare(p1_best_rank.high_card.value, p2_best_rank.high_card.value)
    elif p1_best_rank.rank == 9: # straight flush
        winner = compare(p1_best_rank.straight_flush["high"], p2_best_rank.straight_flush["high"])
    # no royal flush tie possible
    return winner


def get_card_list(card_objects_list):
    card_list = []
    for card in card_objects_list:
        card_list.append(card.get_card())
    return card_list


def perform_stage(first, second, pot, cards):
    time.sleep(1)
    player_folded = False
    ai_folded = False
    previous_action = "CHECK"
    bet = 0
    if (first.name == "AI"):
        while True:
            previous_bet = bet
            bet = ai_response(first, second, previous_action, bet, pot, cards)
            previous_action = determine_action(bet, previous_action, previous_bet)
            if previous_action == "FOLD":
                ai_folded = True
                break
            pot += handle_action(first, previous_action, bet)
            if previous_action == "CALL":
                break

            previous_bet = bet
            bet = player_response(second, bet)
            previous_action = determine_action(bet, previous_action, previous_bet)
            if previous_action == "FOLD":
                player_folded = True
                break
            pot += handle_action(second, previous_action, bet)
            if previous_action == "CALL" or previous_action == "CHECK":
                break

    else:
        while True:
            time.sleep(1)
            previous_bet = bet
            bet = player_response(first, bet)
            previous_action = determine_action(bet, previous_action, previous_bet)
            if previous_action == "FOLD":
                player_folded = True
                break
            pot += handle_action(first, previous_action, bet)
            if previous_action == "CALL":
                break
            
            # Have the AI determine what action it should take
            previous_bet = bet
            bet = ai_response(second, first, previous_action, bet, pot, cards)
            previous_action = determine_action(bet, previous_action, previous_bet)
            if previous_action == "FOLD":
                ai_folded = True
                break
            pot += handle_action(second, previous_action, bet)
            if previous_action == "CALL" or previous_action == "CHECK":
                break
    return [pot, player_folded, ai_folded]



def player_response(player, previous_bet):
    bet = int(input("How much will you bet? [-1 to fold]"))
    if previous_bet > 0 and not bet == -1 and bet < previous_bet and bet < player.stack:
        bet = previous_bet
    amount = bet if bet < player.stack else player.stack
    return amount

def ai_response(ai, player, action, bet, pot, cards):
    ai_action = ai.determine_action(player, action, bet, pot, cards)
    if ai_action == "FOLD":
        time.sleep(1)
        print("\nThe AI folds. Player wins the pot.\n")
        time.sleep(1)
        return -1
    elif ai_action == "RAISE":
        time.sleep(1)
        if action == "RAISE":
            bet = 2 * bet
            bet = bet if bet < ai.stack else ai.stack
        else:
            bet = math.ceil(pot/2)
        print("\nThe AI raises {}".format(bet))
        time.sleep(1)
        return bet
    elif ai_action == "CHECK" or bet == 0:
        time.sleep(1)
        print("\nThe AI checks.\n")
        time.sleep(1)
        return 0
    elif ai_action == "CALL":
        time.sleep(1)
        bet = bet if bet < ai.stack else ai.stack
        print("\nThe AI calls {0}.\n".format(bet))
        time.sleep(1)
        return bet
    
def determine_action(bet, previous_action, previous_bet):
    if bet == 0:
        return "CHECK"
    elif bet == -1:
        return "FOLD"
    else:
        if previous_action == "RAISE":  # Need to add a condition to check if raise size was legal
            if 2 * previous_bet <= bet:
                return "RAISE"
            return "CALL"
        return "RAISE"
    
def handle_action(player, action, bet):
    if action == "CALL" or action == "RAISE":
        player.bet(bet)
        if (player.stack == 0):
            print("{0} is all in".format(player.name))
        return bet        
    else:
        return 0
    
def check_for_fold(result):
    return result[1] or result[2]
    
def print_stage():
    # Uncomment to hide AI hand

    if (p1.name == "AI"):
        print("{1} \t({0})\tCards: \t[ ? , ? ]".format(
            p1.stack, p1.name))
        print("{2} \t({1})\tCards: \t{0}".format(
            get_card_list(p2.hand.in_hand), p2.stack, p2.name))
    else:
        print("{2} \t({1})\tCards: \t{0}".format(
            get_card_list(p1.hand.in_hand), p1.stack, p1.name))
        print("{1} \t({0})\tCards: \t[ ? , ? ]".format(
            p2.stack, p2.name))
        
    # Comment when hiding AI hands
    # print("{2} \t({1})\tCards: \t{0}".format(
    #         get_card_list(p1.hand.in_hand), p1.stack, p1.name))
    # print("{2} \t({1})\tCards: \t{0}".format(
    #         get_card_list(p2.hand.in_hand), p2.stack, p2.name))



if __name__ == '__main__':

    # start timer for program execution
    start_time = time.time()

    player_1 = Agent.Agent("AI")
    player_1.swap_button()
    button = 1
    player_name = input("What is the name of the player? ")
    player_2 = Player.Player(player_name)
    player_1.load_player_data(player_name)

    round = 1

    while (can_play(player_1) & can_play(player_2)):
        pot = 0
        in_deck = Deck.Deck()
        in_play = []
        in_discard = []
        folded = False

        print("\tHand: [{0}]".format(round))

        # Set player order
        p1 = player_1 if player_1.is_button() else player_2
        p2 = player_1 if p1 == player_2 else player_2

        # PREFLOP STAGE
        print("---------------\nStage: Preflop")
        deal_to_player(p1)
        deal_to_player(p2)
        deal_to_player(p1)
        deal_to_player(p2)
        # Put blinds into the pot
        p1.bet(1)
        p2.bet(1)
        pot = 2
        print("Putting in blinds...")
        print("Total pot: {0}\n".format(pot))
        time.sleep(1)
        # show player hole cards
        print_stage()
        print()
        # Preform preflop actions
        result = perform_stage(p1, p2, pot, in_play)
        pot = result[0]
        folded = check_for_fold(result)
        print("Total pot: {0}".format(pot))

        # Handle exploitations
        if p1.name == "AI":
            p1.playing_hand(not result[1])
        else:
            p2.playing_hand(not result[1])

        # FLOP STAGE
        if (not folded):
            print("---------------\nStage: Flop")
            # show player hole cards
            print_stage()
            # Perform flop actions
            deal_flop()
            if not (p1.stack == 0 or p2.stack == 0):
                result = perform_stage(p1, p2, pot, in_play)
                pot = result[0]
                folded = check_for_fold(result)
            print("Total pot: {0}\n".format(pot))

        # TURN STAGE
        if (not folded):
            print("---------------\nStage: Turn")
            # show player hole cards
            print_stage()
            # Perform turn actions
            deal_turn()
            if not (p1.stack == 0 or p2.stack == 0):
                result = perform_stage(p1, p2, pot, in_play)
                pot = result[0]
                folded = check_for_fold(result)
            print("Total pot: {0}\n".format(pot))

        # RIVER STAGE
        if (not folded):
            print("---------------\nStage: River")
            # show player hole cards
            print_stage()
            # Perform river actions
            deal_river()
            if not (p1.stack == 0 or p2.stack == 0):
                result = perform_stage(p1, p2, pot, in_play)
                pot = result[0]
                folded = check_for_fold(result)
            print("Total pot: {0}\n".format(pot))

        if (folded):
            if result[1]:
                # Player has folded
                print("Player has folded. AI wins a pot of {0}".format(pot))
                if p1.name == "AI":
                    p1.stack += pot
                else:
                    p2.stack += pot
            elif result[2]:
                # AI has folded
                print("AI has folded. Player wins a pot of {0}".format(pot))
                if p1.name == "Player":
                    p1.stack += pot
                else:
                    p2.stack += pot
        else:
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
        time.sleep(1)
    
    if p1.stack > p2.stack:
        print("---------------\nPlayer 1 wins!\n---------------")
    else:
        print("---------------\nPlayer 2 wins!\n---------------")

    # Save player data
    player_1.save_player_data()

    # end timer
    print("--- Execution Time: {0} ---".format(
        datetime.timedelta(seconds=(time.time() - start_time))))
