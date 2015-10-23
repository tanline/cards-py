from cards.game import Game
from cards.deck import Deck
import unittest

class TestGame(unittest.TestCase):
    def test_game_creation(self):
        deck = Deck()
        game = Game(deck)
        self.assertIsNotNone(game)
        self.assertEqual(game.number_of_players(), 0)

    def test_start_game(self):
        deck = Deck()
        game = Game(deck)
        self.assertRaises(NotImplementedError, game.start_game)

if __name__ == '__main__':
    unittest.main()
