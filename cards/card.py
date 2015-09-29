class Card(object):

    SUITS = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self, suit, value):
        self.__value = value
        self.__suit = suit

    # Define print function for class
    def __str__(self):
        if self.__value == 1:
            card_name = "Ace"
        elif self.__value == 11:
            card_name = "Jack"
        elif self.__value == 12:
            card_name = "Queen"
        elif self.__value == 13:
            card_name = "King"
        else:
            card_name = str(self.__value)
        return card_name + " of " + self.__suit

    # Define comparison functions for class
    def __lt__(self, other):
        return self.__value < other.__value

    def __le__(self, other):
        return self.__value <= other.__value

    def __eq__(self, other):
        return self.__value == other.__value

    def __ne__(self, other):
        return self.__value != other.__value

    def __gt__(self, other):
        return self.__value > other.__value

    def __ge__(self, other):
        return self.__value >= other.__value
