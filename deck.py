import random

from card import Card

# I used tuple because those are the only options for card types
card_types = ("Clubs", "Diamonds", "Hearts", "Spades")


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for kind in card_types:
            for value in range(1, 14):
                # building the deck with Card 1 of Clubs, Card 2 of Clubs
                self.cards.append(Card(kind, value))

    def show_cards(self):
        for card in self.cards:
            card.display()

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:  # if list is empty it will raise IndexError: pop from empty list
            return self.cards.pop()
