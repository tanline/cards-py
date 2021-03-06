from player import Player
from deck import Deck

class Game(object):
    def __init__(self, deck):
        self._min_players = 1
        self._max_players = 4
        self._players = {}
        self.deck = deck

    def add_player(self, player):
        self._players[player.id()] = player

    def remove_player(self, player):
        del self._players[player.id()]

    def number_of_players(self):
        return len(self._players)

    def start_game(self):
        raise NotImplementedError

    def all_players_still_have_cards(self):
        if (self.number_of_players() == 0):
            return 0
        else:
            for _p_id, p_obj in self._players.iteritems():
                if (p_obj['player'].size_of_hand() > 0):
                    return 0
            return 1

class War(Game):
    def __init__(self):
        Game.__init__(self, Deck())
        self._max_players = 2
        self._min_players = 2
        self._player_order = []

    def start_game(self):
        print "Welcome to WAR!"
        print "-"*20
        self.create_players()
        print "The first player is:", self._players[0]['player'].name
        print "The first player is:", self._players[1]['player'].name
        print "-"*20
        print "Here is the scoreboard:"
        self.print_scores()
        print "-"*20
        self.deal_cards()
        self.begin_playing()

    def create_players(self):
        name = raw_input("What is Player 1's name? ")
        self.add_player(Player(name, 0))
        name = raw_input("What is Player 2's name? ")
        self.add_player(Player(name, 1))

    def add_player(self, player):
        if self.number_of_players() < self._max_players:
            player_object = {'player': player, 'score': 0}
            self._players[player.id()] = player_object
            self._player_order.append(player.id())

    def begin_playing(self):
        while(self.all_players_still_have_cards()):
            p1_card = self._players[0]['player'].take_top_card()
            p2_card = self._players[1]['player'].take_top_card()
            if (p1_card > p2_card):
                self._players[0]['player'].give_card(p1_card, 1)
                self._players[0]['player'].give_card(p2_card, 1)
            elif (p2_card > p1_card):
                self._players[1]['player'].give_card(p1_card, 1)
                self._players[1]['player'].give_card(p2_card, 1)
            else:
                self.begin_war()

        if (self._players[0]['player'].size_of_hand() ==  0):
            print "Your Winner is....." + self._players[0]['player'].name + "!!!"
        else:
            print "Your Winner is....." + self._players[1]['player'].name + "!!!"

    # TODO: Improve design of this method
    def begin_war(self):
        face_up_p1 = self._players[0]['player'].take_top_card()
        face_up_p2 = self._players[1]['player'].take_top_card()
        face_down_p1 = self._players[0]['player'].take_top_card()
        face_down_p2 = self._players[1]['player'].take_top_card()

        prize = [face_up_p1, face_up_p2, face_down_p1, face_down_p2]

        if (face_up_p1 > face_up_p2):
            self._players[0]['player'].give_cards(prize, 1)
            return 0
        elif (face_up_p2 > face_up_p1):
            self._players[1]['player'].give_cards(prize, 1)
            return 1
        else:
            if (face_down_p1 > face_down_p2):
                self._players[0]['player'].give_cards(prize, 1)
                return 0
            elif (face_down_p2 > face_down_p1):
                self._players[1]['player'].give_cards(prize, 1)
                return 1
            else:
                winner_index = self.begin_war()
                self._players[winner_index]['player'].give_cards(prize, 1)
                return winner_index

    def deal_cards(self):
        while (self.deck.cards_left() > 0):
            for p_id in self._player_order:
                card = self.deck.deal()
                self._players[p_id]['player'].give_card(card)

    def print_scores(self):
        for p_id, p_obj in self._players.iteritems():
            print p_obj['player'].name + ': ' + str(p_obj['score'])
