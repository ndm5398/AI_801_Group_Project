from Player import Player
import StraightOuts, FlushOuts, BoardTexture
from Rank import Rank
from itertools import combinations
import json
import random
import Hand

class Agent(Player):

    def __init__(self, name):
        Player.__init__(self, name)

    def load_player_data(self, name):
        f = open("player_database.json")
        data = json.load(f)
        self.opponent_name = name
        self.opponent_data = data[name] if name in data.keys() else self.generate_opponent_data()
        print(self.opponent_data)
        f.close()

    def generate_opponent_data(self):
        self.new_opponent = True
        opponent_data = {}
        opponent_data["hands_played"] = 0
        opponent_data["total_hands"] = 0
        return opponent_data
    
    def save_player_data(self):
        f = open("player_database.json")
        data = json.load(f)
        f.close()

        data[self.opponent_name] = self.opponent_data
        with open("player_database.json", "w") as outfile:
            outfile.write(json.dumps(data))
        f.close()

    def determine_action(self, opponent, action, bet, pot, in_play):
        # For pre flop action
        if len(in_play) == 0:
            return self.preflop_evaluate(action)
        
        # Always call really small bets
        if bet > 0 and (bet/pot) <= 0.1:
            return "CALL"

        # For post flop action
        if action == "CHECK":
            # If hand is ahead, then raise, but only 50 percent of the time to remain balanced

            if self.hand_is_ahead(in_play) and random.random() > 0.5:
                return "RAISE"
            return "CHECK"
        elif action == "RAISE":
            # Guess if we are ahead or behind
            # if we are ahead, call
            # else calculate pot odds to determine if we should call
            if self.hand_is_ahead(in_play):
                # print("Assuming our hand is GOOD")
                return "CALL"
            else:
                # print("Assuming our hand is BAD")
                pot_odds = self.calc_pot_odds(pot, bet)
                equity = self.calc_equity(in_play)
                if equity > pot_odds:
                    return "CALL"
                else:
                    # print("Not enough equity to call. AI is folding...")
                    return "FOLD"
    
    # Used to determine if AI should call when player raised preflop
    def preflop_evaluate(self, previous_action):
        self.hand.sort_hand()
        low, high = self.hand.in_hand[0], self.hand.in_hand[1]
        suited = self.hand.is_suited()
        connected = self.hand.is_connected()
        pair, low_broadway = False, False
        if low.value == high.value:
            pair = True
        if low.value > 10:
            low_broadway = True

        #check for broadway combo or pocket pair
        if low_broadway or pair:
            return "RAISE"
        #check suited
        elif suited:
            #check A, K, Q w/ non-broadway or connected
            if (high.value > 11) or connected:
                return "CALL"
            elif previous_action == "RAISE":
                # If the player is a loose player, we want to continue playing here
                return "CALL" if self.get_hands_played_freq() > 0.75 else "FOLD"
            else:
                return "CHECK"
        #check connected cards w/ low greater than 4
        elif connected and (low.value > 4):
            return "CALL"
        elif previous_action == "RAISE":
            return "FOLD"
        else:
            return "CHECK"
    
    def hand_is_ahead(self, in_play):
        # Rank our hand if not in preflop stage
        if len(in_play) > 0:
            rank = self.rank_player_possible_hands(in_play)
            # print("Hand rank: " + str(rank.rank))

            # Flushes are stronger than straights and dry boards, so we check that first
            tones = BoardTexture.board_tone(in_play)
            if len(tones) > 0:
                # Should return false unless we have a flush or greater
                return rank.rank > 5
            elif BoardTexture.board_connectivity(in_play):
                return rank.rank > 4
            elif len(in_play) < 4:
                return rank.rank > 1
            else:
                return rank.rank > 2
        else:
            # Handle special preflop state
            return True

    def calc_pot_odds(self, pot, bet):
        return bet / (bet + pot)

    def calc_equity(self, in_play):
        # If we get to this point and all cards are dealt, we should fold
        if len(in_play) == 5:
            return 0
        # For now calculate the outs to hit straights or flushes, shouldn't be chasing anything else
        outs = self.get_outs_to_a_straight(in_play)
        outs += self.get_outs_to_a_flush(in_play)
        equity = outs * 4 if len(in_play) == 3 else outs * 2
        return equity / 100

    def get_outs_to_a_straight(self, in_play):
        # Cycle through all straight scenarios, if 4 of cards in a scenario are in play or in the hand
        # we found an out. Then determine how many of the 5th card remain in play
        straights = StraightOuts.get_straights(in_play, self.hand.in_hand)
        outs = StraightOuts.get_straight_outs(straights, self.hand.in_hand, in_play)
        return len(outs)

    def get_outs_to_a_flush(self, in_play):
        flushes = FlushOuts.get_flushes(in_play, self.hand.in_hand)
        outs = FlushOuts.get_flush_outs(flushes, self.hand.in_hand, in_play)
        return len(outs)

    def rank_player_possible_hands(self, in_play):
        potential_cards = in_play + self.hand.in_hand
        possible_combinations = list(combinations(potential_cards, 5))
        best_rank = Rank(list(possible_combinations[0]))
        for entry in possible_combinations:
            current_rank = Rank(list(entry))
            if current_rank.rank > best_rank.rank:
                best_rank = current_rank
        return best_rank
    
    def get_hands_played_freq(self):
        return self.opponent_data["hands_played"] / self.opponent_data["total_hands"]
    
    def playing_hand(self, played):
        if played:
            self.opponent_data["hands_played"] += 1
        self.opponent_data["total_hands"] += 1