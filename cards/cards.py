import random

class Deck(object):

    def __init__(self):
        """Creates a standard 52 card deck, and shuffles it into a randomized order
        """
        self.__cards = self.__build_deck()
        self.shuffle()

    def cards_left(self):
        """Returns the number of cards left in the deck

        Returns an integer.
        """
        return len(self.__cards)

    def __build_deck(self):
        """Creates a standard 52 card deck, in a non sorted arrangment
        
        Creates a deck of playing cards.
        """
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        deck = []
        i = 1
        while i < 14:
            for suit in suits:
                card = Card(suit, i)
                deck.append(card)
            i = i + 1
        return deck

    def reset(self):
        """Reset the deck to a shuffled 52-card deck

        Resets all of the cards and shuffles the deck.
        """
        self.__cards = self.__build_deck()
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck.

        Shuffles the deck of card using the standard shuffle method
        """
        random.shuffle(self.__cards)
    
    def peek(self):
        """Print the card at the top of the deck

        Prints the name of the card that is at the top of the deck.
        """
        print self.__cards[self.cards_left() - 1]

    def deal(self):
        """Deal a card from the stack.
        
        Deals the top card from the deck. Returns a Card object
        """
        return self.__cards.pop()

class Card(object):
    
    def __init__(self, suit, value):
        self.__value = value
        self.__suit = suit

    # Define print function for class
    def __str__(self):
        x = self.value
        if x == 1:
            x = "Ace"
        elif x == 11:
            x = "Jack"
        elif x == 12:
            x = "Queen"
        elif x == 13:
            x = "King"
        else:
            x = str(x)
        return x + " of " + self.suit

    # Define comparison functions for class
    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value
    
    def __ne__(self, other):
        return self.value != other.value
    
    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

class Player(object):
    
    def __init__(self, name, human=0):
        self.name = name
        self.cpu = 0
        self.__deck = []

    def add_card(self, card):
        self.__deck.append(card)

d = Deck()

a = Card("Spades", 5)
b = Card("Diamonds", 10)
c = d.deal()

print "Card A is", a
print "Card B is", b
print "Card C is", c
print "Is the value of A less than B?", a<b

