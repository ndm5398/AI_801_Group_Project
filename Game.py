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


def can_play(player):
    return not player.is_stack_empty()


def deal_to_player(player):
    player.hand.add_to_hand(in_deck.deal())


def deal_flop():
    in_discard.append(in_deck.deal())
    for x in range(3):
        in_play.append(in_deck.deal())
    print("In play: {0}\n".format(get_card_list(in_play)))



def deal_turn():
    in_discard.append(in_deck.deal())
    in_play.append(in_deck.deal())
    print("In play: {0}\n".format(get_card_list(in_play)))



def deal_river():
    in_discard.append(in_deck.deal())
    in_play.append(in_deck.deal())
    print("In play: {0}\n".format(get_card_list(in_play)))



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


def perform_stage(first, second, pot, cards):
    time.sleep(1)
    player_folded = False
    ai_folded = False
    previous_action = "CALL"
    if (first.name == "AI"):
        # For now the AI agent will just check if going first
        print("\n{0} checks.".format(first.name))
        while True:
            bet = player_response(first)
            previous_action = determine_action(bet, previous_action)
            if previous_action == "FOLD":
                player_folded = True
                break
            pot += handle_action(first, previous_action, bet)
            # Have the AI determine what action it should take
            if previous_action == "CHECK":
                break
            else:
                bet = ai_response(first, second, previous_action, bet, pot, cards)
                previous_action = determine_action(bet, previous_action)
                if previous_action == "FOLD":
                    ai_folded = True
                    break
                pot += handle_action(second, previous_action, bet)
                if previous_action == "CALL":
                    break

    else:
        while True:
            time.sleep(1)
            bet = player_response(second)
            previous_action = determine_action(bet, previous_action)
            if previous_action == "FOLD":
                player_folded = True
                break
            pot += handle_action(second, previous_action, bet)
            if previous_action == "CHECK":
                break
            else:
                # Have the AI determine what action it should take
                bet = ai_response(second, first, previous_action, bet, pot, cards)
                previous_action = determine_action(bet, previous_action)
                if previous_action == "FOLD":
                    ai_folded = True
                    break
                pot += handle_action(first, previous_action, bet)
                if previous_action == "CALL":
                    break
    return [pot, player_folded, ai_folded]



def player_response(player):
    return int(input("How much will you bet? [-1 to fold]"))

def ai_response(ai, player, action, bet, pot, cards):
    ai_action = ai.determine_action(player, action, bet, pot, cards)
    if ai_action == "FOLD":
        time.sleep(1)
        print("\nThe AI folds. Player wins the pot.\n")
        time.sleep(1)
        return -1
    elif ai_action == "CHECK":
        time.sleep(1)
        print("\nThe AI checks.\n")
        time.sleep(1)
        return 0
    else:
        # Raising is not yet an option
        time.sleep(1)
        print("\nThe AI calls {0}.\n".format(bet))
        time.sleep(1)
        return bet
    
def determine_action(bet, previous_action):
    if bet == 0:
        return "CHECK"
    elif bet == -1:
        return "FOLD"
    else:
        if previous_action == "RAISE":  # Need to add a condition to check if raise size was legal
            return "CALL"
        return "RAISE"
    
def handle_action(player, action, bet):
    if action == "CALL" or action == "RAISE":
        player.bet(bet)
        return bet        
    else:
        return 0
    
def check_for_fold(result):
    return result[1] or result[2]
    
def print_stage():
    # Uncomment to hide AI hand

    # if (p1.name == "AI"):
    #     print("{1} \t({0})\tCards: \t[ ? , ? ]".format(
    #         p1.stack, p1.name))
    #     print("{2} \t({1})\tCards: \t{0}".format(
    #         get_card_list(p2.hand.in_hand), p2.stack, p2.name))
    # else:
    #     print("{2} \t({1})\tCards: \t{0}".format(
    #         get_card_list(p1.hand.in_hand), p1.stack, p1.name))
    #     print("{1} \t({0})\tCards: \t[ ? , ? ]".format(
    #         p2.stack, p2.name))
        
    # Comment when hiding AI hands
    print("{2} \t({1})\tCards: \t{0}".format(
            get_card_list(p1.hand.in_hand), p1.stack, p1.name))
    print("{2} \t({1})\tCards: \t{0}".format(
            get_card_list(p2.hand.in_hand), p2.stack, p2.name))


if __name__ == '__main__':

    # start timer for program execution
    start_time = time.time()

    player_1 = Agent.Agent("AI")
    player_1.swap_button()
    button = 1
    player_2 = Player.Player("Player")
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
        # show player hole cards
        print_stage()
        print()
        # Preform preflop actions
        result = perform_stage(p1, p2, pot, in_play)
        pot = result[0]
        folded = check_for_fold(result)
        print("Total pot: {0}".format(pot))

        # FLOP STAGE
        if (not folded):
            print("---------------\nStage: Flop")
            # show player hole cards
            print_stage()
            # Perform flop actions
            deal_flop()
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
                    if p1_best_rank.high_card.value > p2_best_rank.high_card.value:
                        p1.stack += pot
                        print("\n{0} Wins\n".format(p1.name))
                    elif p2_best_rank.high_card.value > p1_best_rank.high_card.value:
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
        time.sleep(5)

    # end timer
    print("--- Execution Time: {0} ---".format(
        datetime.timedelta(seconds=(time.time() - start_time))))
