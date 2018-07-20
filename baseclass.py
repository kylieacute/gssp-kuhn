class BasePlayer:
    name = None # players should set their bots name
    def play_first(self, moves, hands, card):
        raise NotImplementedError
    def play_second(self, moves, hands, card, opp_move):
        raise NotImplementedError
    # moves is what players did:
    #   first element of each tuple in list is first player

    # moves:
    #  -1: folded
    #   0: checked (if player 1 checks, then calls, they will have the code of called)
    #   1: called
    #   2: bet

    #   these codes also used for opp_move, which is the move player 1 just did that round



    # hands:
    #   there are 3 cards, from 1 to 3 inclusive. you will always no what card you had,
    #   but if either player folded, then you will not know what card your opponent had.
    #   this is represented with a -1.
    #
    #   hands is a list of 2-tuples. the first element in each tuple is your card,
    #   then the opponents card, if applicable.

    # making a move:
    #   to speed things up, your bot, when playing first,
    #   rather than return check or bet, will return check-then-call or check-then-fold or bet
    #   so that you only need one call.
    #
    # first player moves
    #
    #  -1: check then fold if second player bets
    #   1: check then call if player
    #   2: bet
    #
    # yeah i know 0 isn't used here but it's for consistency with the move values from before
    # i also have used anything not in this list as bet, just because of the way i've implemented it
    #
    # second player moves
    # -1: fold
    #  0: check
    #  1: call
    #  2: bet
    #
    # only some of these are available at any one point but c o n s i s t e n c y.
    # make sure you return an acceptable one... i guess i'll allow call and check to be interchangeable.
    # and bet and call if the other bot has bet... it looks better if you use the right one though i guess