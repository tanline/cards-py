from player import Player

class Game(object):

    def __init__(self, deck, game_type=None):
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
