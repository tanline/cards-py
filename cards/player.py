class Player(object):

    def __init__(self, name, human=0):
        self.name = name
        self.cpu = human
        self.__hand = []
        self.__number_of_cards_in_hand = 0

    def change_name(self, name):
        self.name = name

    def make_human(self):
        self.cpu = 0

    def make_cpu(self):
        self.cpu = 1

    def add_card(self, card):
        self.__hand.append(card)
        self.__number_of_cards_in_hand += 1

    def remove_card(self, card):
        self.__hand.remove(card)
        self.__number_of_cards_in_hand -= 1

    def number_of_cards_in_hand(self):
        self.__number_of_cards_in_hand
