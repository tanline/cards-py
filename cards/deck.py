import random
from card import Card

class Deck(object):

    def __init__(self):
        """Creates a standard 52 card deck, and shuffles it into a randomized order

        Returns a Deck.
        """
        self._cards = self.build_deck()
        self.shuffle()

    def cards_left(self):
        """Returns the number of cards left in the deck

        Returns an integer.
        """
        return len(self._cards)

    def build_deck(self):
        """Creates a standard 52 card deck, in a non sorted arrangment

        Creates a deck of playing cards.
        """
        deck = []
        i = 1
        while i < 14:
            for suit in Card.SUITS:
                card = Card(suit, i)
                deck.append(card)
            i = i + 1
        return deck

    def reset(self):
        """Reset the deck to a shuffled 52-card deck

        Resets all of the cards and shuffles the deck.
        """
        self._cards = self._build_deck()
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck.

        Shuffles the deck of card using the standard shuffle method
        """
        random.shuffle(self._cards)

    def peek(self):
        """Print the card at the top of the deck

        Prints the name of the card that is at the top of the deck.
        """
        return self._cards[self.cards_left() - 1]

    def deal(self):
        """Deal a card from the top of the deck.

        Deals the top card from the deck. Returns a Card object
        """
        return self._cards.pop()
