class Card(object):

    SUITS = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self, suit, value):
        self._value = value
        self._suit = suit

    # Define print function for class
    def __str__(self):
        if self._value == 1:
            card_name = "Ace"
        elif self._value == 11:
            card_name = "Jack"
        elif self._value == 12:
            card_name = "Queen"
        elif self._value == 13:
            card_name = "King"
        else:
            card_name = str(self._value)
        return card_name + " of " + self._suit

    # Define comparison functions for class
    def __lt__(self, other):
        return self._value < other._value

    def __le__(self, other):
        return self._value <= other._value

    def __eq__(self, other):
        return self._value == other._value

    def __ne__(self, other):
        return self._value != other._value

    def __gt__(self, other):
        return self._value > other._value

    def __ge__(self, other):
        return self._value >= other._value

    def value(self):
        return self._value

    def suit(self):
        return self._suit
