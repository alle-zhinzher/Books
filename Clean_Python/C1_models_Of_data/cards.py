import collections
Card = collections . namedtuple(' Card ', ['rank', 'suit'])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list(’ JQKA ')
    suits = 'spades diamonds clubs hearts 1'.split()


def _ init _(self):


self._cards = [Cardfrank, suit) for suit in self. suits
for rank in self.ranks]
def
_ len _(self):
return len(self ._cards)
