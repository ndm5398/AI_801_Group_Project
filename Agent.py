from Player import Player
import StraightOuts


class Agent(Player):

    def __init__(self, name):
        Player.__init__(self, name)

    def determine_action(self, opponent, action, bet, pot, in_play):
        if action == "CHECK":
            # Should check for now
            return "CHECK"
        elif action == "RAISE":
            # Guess if we are ahead or behind
            # if we are ahead, call
            # else calculate pot odds to determine if we should call
            if self.hand_is_ahead():
                return "CALL"
            else:
                pot_odds = self.calc_pot_odds(pot, bet)
                equity = self.calc_equity(self, in_play)
                if equity > pot_odds:
                    return "CALL"
                else:
                    return "FOLD"

    def hand_is_ahead():

        return True

    def calc_pot_odds(pot, bet):
        return bet / (bet + pot)

    def calc_equity(self, in_play):
        # If we get to this point and all cards are dealt, we should fold
        if in_play.length == 5:
            return 0
        # For now calculate the outs to hit straights or flushes, shouldn't be chasing anything else
        outs = self.get_outs_to_a_straight(self, in_play)
        outs += self.get_outs_to_a_flush(self, in_play)
        equity = outs * 4 if in_play.length == 3 else outs * 2
        return equity / 100

    def get_outs_to_a_straight(self, in_play):
        # Cycle through all straight scenarios, if 4 of cards in a scenario are in play or in the hand
        # we found an out. Then determine how many of the 5th card remain in play
        straights = StraightOuts.get_straights(in_play, self.hand)
        outs = StraightOuts.get_straight_outs(straights, self.hand, in_play)
        return outs

    def get_outs_to_a_flush(self, in_play):
        return 0
