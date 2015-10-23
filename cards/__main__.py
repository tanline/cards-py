from deck import Deck
from game import Game

if __name__ == '__main__':
    d = Deck()
    # a = d.deal()
    # b = d.deal()
    # c = d.deal()

    # print "Card A is", a
    # print "Card B is", b
    # print "Card C is", c
    # print "Is the value of A less than B?", a<b
    # print "Is the value of A less than C?", a<c
    # print "Is the value of A less than B?", a<b
    # print "Is the value of B less than C?", b<c

    game = Game(d)
    print "Number of players in the game", game.number_of_players()
    print "Cards left in deck", game.deck.cards_left()

    test = game.deck
    a = test.deal()
    b = test.deal()
    c = test.deal()
    print game.deck.peek()
    print test.peek()
    print d.peek()
    print game.deck == test.peek
    print "Cards left in deck", game.deck.cards_left()
    print "Cards left in test deck", test.cards_left()
