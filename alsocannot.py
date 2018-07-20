from baseclass import BasePlayer
class cannotplay2(BasePlayer):
    name = "also cannot play"
    def play_first(self, moves, hands, card):
        return -1
    def play_second(self, moves, hands, card, opp_move):
        if opp_move==2:
            return 1
        else:
            return 2