from deck import Deck

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle_cards()
    card = deck.draw_card()
    card.display()  # display the drawn card
    print('\n')
    deck.show_cards()  # display the rest of the cards
