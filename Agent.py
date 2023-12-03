from Player import Player
import StraightOuts, FlushOuts, BoardTexture
from Rank import Rank
from itertools import combinations

class Agent(Player):

    def __init__(self, name):
        Player.__init__(self, name)

    def determine_action(self, opponent, action, bet, pot, in_play):
        if action == "CHECK":
            # Should check for now
            if self.hand_is_ahead(in_play):

                return "RAISE"
            return "CHECK"
        elif action == "RAISE":
            # Guess if we are ahead or behind
            # if we are ahead, call
            # else calculate pot odds to determine if we should call
            if self.hand_is_ahead(in_play):
                print("Assuming our hand is GOOD")
                return "CALL"
            else:
                print("Assuming our hand is BAD")
                pot_odds = self.calc_pot_odds(pot, bet)
                equity = self.calc_equity(in_play)
                if equity > pot_odds:
                    return "CALL"
                else:
                    print("Not enough equity to call. AI is folding...")
                    return "FOLD"
    
    def hand_is_ahead(self, in_play):
        # Rank our hand if not in preflop stage
        if len(in_play) > 0:
            rank = self.rank_player_possible_hands(in_play)
            print("Hand rank: " + str(rank.rank))

            # Flushes are stronger than straights and dry boards, so we check that first
            tones = BoardTexture.board_tone(in_play)
            if len(tones) > 0:
                # Should return false unless we have a flush or greater
                return rank.rank > 5
            elif BoardTexture.board_connectivity(in_play):
                return rank.rank > 4
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