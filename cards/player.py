class Player(object):

    def __init__(self, name, human=0):
        self._id = 0
        self.name = name
        self.human = human
        self._hand = []
        self._hand_size = 0

    def set_name(self, name):
        self.name = name

    def set_human(self):
        self.human = 1

    def give_card(self, card):
        self._hand.append(card)
        self._hand_size+= 1

    def take_card(self, card):
        self._hand.remove(card)
        self._hand_size-= 1

    def size_of_hand(self):
        return self._hand_size

    def id(self):
        return self._id
