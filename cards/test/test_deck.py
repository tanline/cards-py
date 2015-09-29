from nose.tools import *
from cards.deck import *

def test_deck():
    deck = Deck()
    assert_equal(deck.cards_left(), 52)

