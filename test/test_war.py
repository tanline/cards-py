from cards.game import War
from cards.player import Player
import unittest

class TestWar(unittest.TestCase):
    def test_game_creation(self):
        game = War()
        self.assertIsNotNone(game)

    def test_add_players(self):
        game = War()
        p1 = Player("One", 1)
        p2 = Player("Two", 2)
        p3 = Player("Three", 3)
        game.add_player(p1)
        self.assertIn(p1.id(), game._player_order)
        self.assertIs(p1, game._players[p1.id()]['player'])
        game.add_player(p2)
        self.assertIn(p2.id(), game._player_order)
        self.assertIs(p2, game._players[p2.id()]['player'])
        game.add_player(p3)
        self.assertNotIn(p3.id(), game._player_order)
        self.assertEqual(2, len(game._players))

if __name__ == '__main__':
    unittest.main()
