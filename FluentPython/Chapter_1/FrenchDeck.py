"""
A Frenchdeck is the common poke we played in the daily life, it contains 52 cards totally, with 4 suits, each suit
contains 13 cards from 2 - 10, and J, Q, K, A. Some of them also contains 2 cards one is the king one is the queen ( in
this case it's 54 cards totally).
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    # print how many cards in a FrenchDeck class
    deck = FrenchDeck()
    print(len(deck))
    # get a card from deck, i.g deck[0] is the first card, deck[-1] is the last card.
    print(deck[0])
    print(deck[-1])
