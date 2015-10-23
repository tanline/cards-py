from player import Player
from deck import Deck

class Game(object):

    def __init__(self, deck):
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

class War(Game):
    def __init__(self):
        Game.__init__(self, Deck())
        self._max_players = 2

    def start_game(self):
        print "Welcome to WAR!"
        self.create_players()
        print "The first player is:", self._players[0]['player'].name
        print "The first player is:", self._players[1]['player'].name
        print "Here is the scoreboard:"
        self.print_scores()

    def create_players(self):
        name = raw_input("What is Player 1's name? ")
        self.add_player(Player(name, 0))
        name = raw_input("What is Player 2's name? ")
        self.add_player(Player(name, 1))

    def add_player(self, player):
        if self.number_of_players() < self._max_players:
            player_object = {'player': player, 'score': 0}
            self._players[player.id()] = player_object

    def print_scores(self):
        for p_id, p_obj in self._players.iteritems():
            print p_obj['player'].name + ': ' + str(p_obj['score'])
