import time
import datetime
import random
import Deck
import Card
import Hand
import Player
from Agent import Agent
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


def perform_stage(first, second, pot, cards):
    time.sleep(1)
    if (first.name == "player"):
        not_complete = True
        previous_action = "CALL"
        while not_complete:
            bet = player_response(first)
            previous_action = determine_action(bet, previous_action)
            handle_action(first, previous_action, bet)
            # Have the AI determine what action it should take
            bet = ai_response(first, second, previous_action, bet, pot, cards)
            previous_action = determine_action(bet)
            handle_action(second, previous_action, bet)

    else:
        # For now the AI agent will just check if going first
        print("{0} checks.".format(first.name))
        time.sleep(1)
        bet = int(input("How much will you bet? [-1 to fold]"))


def player_response(player, pot):
    return int(input("How much will you bet? [-1 to fold]"))

def ai_response(ai, player, action, bet, pot, cards):
    ai_action = ai.determine_action(player, action, bet, pot, cards)
    if ai_action == "FOLD":
        return -1
    elif ai_action == "CHECK":
        return 0
    else:
        return bet
    
def determine_action(bet, previous_action):
    if bet == 0:
        return "CHECK"
    elif bet == -1:
        return "FOLD"
    else:
        if previous_action == "CALL":
            return "RAISE"
    
def handle_action(player, action, bet):
    pass

if __name__ == '__main__':

    # start timer for program execution
    start_time = time.time()

    player_1 = Agent("player")
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

        pot = perform_stage(p1, p2, pot, in_play)
        # intial betting
        bet = int(input("How much will you bet?"))
        pot += p1.bet(bet)
        # p2 is always calling for now until AI is implemented
        time.sleep(1)
        print("AI calls {0}".format(bet))
        pot += p2.bet(bet)
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

        bet = int(input("How much will you bet?"))
        pot += p1.bet(bet)
        # p2 is always calling for now until AI is implemented
        time.sleep(1)
        print("AI calls {0}".format(bet))
        pot += p2.bet(bet)
        print("Total pot: {0}\n".format(pot))

        # TURN STAGE
        print("---------------\nStage: Turn")
        # show player hole cards
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p1.hand.in_hand), p1.stack, p1.name))
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p2.hand.in_hand), p2.stack, p2.name))
        deal_turn()
        print("In play: {0}".format(get_card_list(in_play)))

        bet = int(input("How much will you bet?"))
        pot += p1.bet(bet)
        # p2 is always calling for now until AI is implemented
        time.sleep(1)
        print("AI calls {0}".format(bet))
        pot += p2.bet(bet)
        print("Total pot: {0}\n".format(pot))

        # RIVER STAGE
        print("---------------\nStage: River")
        # show player hole cards
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p1.hand.in_hand), p1.stack, p1.name))
        print("{2} \t({1})\tHole Cards: \t{0}".format(
            get_card_list(p2.hand.in_hand), p2.stack, p2.name))
        deal_river()
        print("In play: {0}".format(get_card_list(in_play)))

        bet = int(input("How much will you bet?"))
        pot += p1.bet(bet)
        # p2 is always calling for now until AI is implemented
        print("AI calls {0}".format(bet))
        pot += p2.bet(bet)
        print("Total pot: {0}\n".format(pot))

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

    # end timer
    print("--- Execution Time: {0} ---".format(
        datetime.timedelta(seconds=(time.time() - start_time))))
