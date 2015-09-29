from nose.tools import *
from cards.card import *

def test_card():
    a = Card("Spades", 10)
    assert_equal(a.value, 10)
    assert_equal(a.suit, "Spades")

def test_card_equalities():
    a = Card("Spades", 10)
    b = Card("Hearts", 13)
    assert_equal(a > b, False)
    assert_equal(a < b, True)
    assert_equal(a != b, True)

