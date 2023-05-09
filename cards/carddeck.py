#!/usr/bin/env python

"""
_summary_ = /
This is an example to show how you can create a deck 
of cards using native python datatypes instead of creating custom objects and methods.

The benefits of this are being able to use slicing, iterators and other built in methods.
"""

import collections

from random import choice

# Define a card object that has just 2 attributes. The rank, and the suit.
Card = collections.namedtuple('Card',['rank', 'suit'])

# Define a deck of cards. By defining a __getitem__ method that is passed 
# directly to a list, we can slice, pick and iterate over the cards like we would any other list. 
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    
    def __getitem__(self, position):
        return self._cards[position]
    

if __name__ == '__main__':
    
    print("Create a card (7 of diamonds)")
    # Create a card
    beer_card = Card('7', 'diamonds')
    
    # Print out an individual card
    print(beer_card)
    
    
    print("\nCreate and print a whole deck of cards.")
    # Create a whole deck of cards
    deck = FrenchDeck()
        
    # Print each of the cards in the deck
    for card in deck:
        print(card)
    
    
    print("\nHow many cards in the deck ?")
    # How many cards are in the deck ? 
    print(len(deck))
    
    
    print("\nPick a random card")    
    # Pick a random card from the deck
    print(choice(deck))
    
    print("\nPrint the first 21 cards")
    # Print 19 cards
    for card in deck[0:20]:
        print(card)