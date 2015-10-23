from cards.card import Card
import unittest

class TestCard(unittest.TestCase):

    def test_card_creation(self):
        a = Card("Spades", 10)
        self.assertEqual(a.value(), 10)
        self.assertEqual(a.suit(), "Spades")

    def test_card_equalities(self):
        a = Card("Spades", 10)
        b = Card("Hearts", 13)
        self.assertEqual(a > b, False)
        self.assertEqual(a < b, True)
        self.assertEqual(a != b, True)

if __name__ == '__main__':
    unittest.main()
