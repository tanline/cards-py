from deck import Deck

if __name__ == '__main__':
    d = Deck()
    a = d.deal()
    b = d.deal()
    c = d.deal()

    print "Card A is", a
    print "Card B is", b
    print "Card C is", c
    print "Is the value of A less than B?", a<b
    print "Is the value of A less than C?", a<c
    print "Is the value of A less than B?", a<b
    print "Is the value of B less than C?", b<c
