from Cards.deck import Deck
import unittest

class TestDeck(unittest.TestCase):

    def test_deck(self):
        deck = Deck()
        self.assert_equal(deck.cards_left(), 52)

if __name__ == '__main__':
    unittest.main()
