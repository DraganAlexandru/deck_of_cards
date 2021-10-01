import unittest

from card import Card
from deck import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_build_entire_deck(self):
        self.assertEqual(52, len(self.deck.cards))

    def test_shuffle_deck(self):
        self.assertNotEqual(self.deck.cards, self.deck.shuffle_cards())

    def test_count_cards_changed(self):
        self.assertEqual(52, len(self.deck.cards))
        self.deck.draw_card()
        self.assertNotEqual(52, len(self.deck.cards))

    def test_instance_of_drawn_card(self):
        self.assertIsInstance(self.deck.draw_card(), Card)


if __name__ == '__main__':
    unittest.main()
