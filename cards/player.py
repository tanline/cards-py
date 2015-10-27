class Player(object):
    def __init__(self, name, id=0, human=0):
        self._id = id
        self.name = name
        self.human = human
        self._hand = []
        self._hand_size = 0

    def set_name(self, name):
        self.name = name

    def set_human(self):
        self.human = 1

    def give_card(self, card, place_at_bottom=0):
        if place_at_bottom:
            self._hand.insert(0, card)
        else:
            self._hand.append(card)
        self._hand_size+= 1

    def give_cards(self, cards, place_all_at_bottom=0):
        for card in cards:
            self.give_card(card, place_all_at_bottom)

    def take_card(self, card):
        self._hand.remove(card)
        self._hand_size-= 1

    def take_top_card(self):
        self._hand_size-= 1
        return self._hand.pop()

    def size_of_hand(self):
        return self._hand_size

    def id(self):
        return self._id
