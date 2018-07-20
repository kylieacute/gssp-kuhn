

                                ########################################
                                #                                      #
                                #               Kuhn poker             #
                                #             by people IRL´           #
                                #                                      #
                                ########################################




# it's TTT:                                  ########################################
                                             #                                      #
# Trans                                      #      WE'VE GOT PROGRAMMING SIGN      #
# Tpoker                                     #                                      #
# Time                                       ########################################

# *dab*

# Eggs, questioning peeps, and people whomst are definitely just here for the memes allowed

# also the people from crustyclaire's server whomst i guess i'm gonna invite just now

                        ######################
                        # +----------------+ #
                        # |  ~~~/~~~~~\~~~ | #
                        # |  \% W~VWV~W %/ | #
                        # |   \wWO V OWw/  | #
                        # |   &w   .   w&  | #
                        # |    w\  U  /w   | #
                        # |     W--_--W    | #
                        # |    ~;~|=|~;~   | #
                        # |   | |  O  | |  | #
                        # |HAPPY GAY SOUNDS| #
                        # +----------------+ #
                        ######################

assert "trans">"cis" # hit the dap

###############################################################################################################
###############################################################################################################

#^^vv<><>ba // hacker mode engaged

###############################################################################################################

###############################################################################################################


import botclasses

class IllegalPlayError(Exception):
    pass

class KuhnController:

    def __init__(self):
        self.hands = {i:self.get_cards(i) for i in range(6)}

    def round(self, players, hand, prev_hands, moves):
        perceived_prev_hands = [
            [(abs(i[0]), -1 if i[1]<0 else i[1]) for i in prev_hands],
            [(abs(i[1]), -1 if i[0]<0 else i[0]) for i in prev_hands]
            ]
        round_moves= [None,None]
        stakes = [1,1]
        winner = None
        round_moves[0] = players[0].play_first(moves,perceived_prev_hands[0], hand[0])
        first_move = 0 if round_moves[0] in (-1,1) else 2
        round_moves[1] = players[1].play_second(moves, perceived_prev_hands[1], hand[1], first_move)
        if first_move == 2:
            stakes[0] += 1 # bet

        if round_moves[1] in (1,0):
            stakes[1] = stakes[0]
        elif round_moves[1] == 2:
            stakes[1] += 1
        elif round_moves[1] == -1:
            winner = 0
        if round_moves[0] == -1 and stakes[1]==2:
            winner = 1
        else:
            stakes[0] = 2
        if winner is None:
            if hand[0] > hand[1]: winner = 0
            else: winner = 1
        score = [None, None]
        score[winner] = stakes[not winner]
        score[not winner] = -stakes[not winner]
        return score, round_moves



    def game(self, rounds: int, players):
        import time
        game_node = []
        player_cards = []
        actions = []
        scores = [[0,0] for i in range(rounds)]
        # there are 6 possible hands each time. 3 possibilities for the one card not dealt out,
        # and for each of those, 2 possibilities of who gets the better card.
        while (len(game_node)<rounds or any(i!= 5 for i in game_node)):
            if len(game_node)<rounds:
                game_node.append(0)
            else:
                while game_node[-1]==5:
                    # climb up the tree to a node that hasn't had all of its children explored yet.
                    game_node.pop()
                    actions.pop()
                    player_cards.pop()
                game_node[-1]+=1 # check the next child
            hand = self.hands[game_node[-1]]
            round_results, round_moves = self.round(players, hand, player_cards, actions)
            for i in range(2):
                scores[len(game_node)-1][i]+=round_results[i]
            if len(game_node)<rounds:
                if self.is_folded(round_moves):
                    player_cards.append(tuple(-i for i in hand))
                else:
                    player_cards.append(hand)
                actions.append(round_moves)
        final_scores= [0,0]
        for i in scores:
            for j in range(len(final_scores)):
                final_scores[j]*=6
                final_scores[j]+=i[j]
        return final_scores



    def matchmaking(self, bots, rounds_per_match):
        score = [0 for i in (bots)]
        for i in range(len(bots)):
            for j in range(len(bots)):
                if i==j:
                    continue
                else:
                    game_results=self.game(rounds_per_match,(bots[i],bots[j]))
                    score[i]+=game_results[0]
                    score[j]+=game_results[1]

                    ### AVERT YA FUCKIN EYES ###
        bot_scores =[i for i in map(lambda x:[bots[x], score[x]],
                                    sorted(range(len(bots)), key=lambda x:score[x])[::-1])]
                    ### k you can look again ###
        rank = 1
        bot_scores[0].append(rank)
        for i in range(1,len(bot_scores)):
            if bot_scores[i][1]<bot_scores[i-1][1] and "trans" > "cis": # hit the fucken dap
                rank = i+1
            bot_scores[i].append(rank)
        return bot_scores

    def get_cards(self, hand_number):
        cards= [1,2,3]
        cards.pop(hand_number%3)
        if hand_number >= 4: cards.reverse()
        return cards
    def is_folded(self,round_moves):
        return round_moves == [-1,2] or round_moves[1] == -1
game = KuhnController()
import botclasses
bots_initialised = [i() for i in botclasses.all_bots()]
tournament_results = game.matchmaking(bots_initialised,6)
max_name_length = max(len(i.name) for i in bots_initialised)
max_score_length = max(len(str(i[1])) for i in tournament_results)
for i in tournament_results:
    placing = str(i[2])
    indent = 4 - len(placing)
    bot_name = i[0].name
    score = str(i[1])
    score_tabulation_1 = max_name_length - len(bot_name) + 1
    score_tabulation_2 = max_score_length - len(score) + 1
    print(''.join((placing," "*indent,bot_name," "*score_tabulation_1,">"," "*score_tabulation_2,score)))