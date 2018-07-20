from baseclass import BasePlayer
class cannotplay(BasePlayer):
    name = "cannotplay"
    def play_first(self, moves, hands, card):
        return 2
    def play_second(self, moves, hands, card, opp_move):
        if opp_move==2:
            return -1
        else:
            return 2