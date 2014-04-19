import unittest
from deck import Deck
from players import Player, BlackJackDealer, BlackJackPlayer

dealer = BlackJackDealer()
player = BlackJackPlayer()
deck = Deck()

#test Deck Class
deck.load_deck()
for card in range(0,deck.cards_in_deck):
	print card
	print deck.deal()
	print deck.index
	print deck.cards_in_deck
	print deck.deck
deck.deal()	
deck.shuffle()	
print deck.deck

#test Player Class

for card in range(0,4):
	dealt_card = deck.deal()
	print dealt_card
	player.add_card_to_hand(dealt_card)
player.display_hand()
print player.get_hand_value()

#test Dealer
deck.load_deck()
for card in range(0,2):
	dealt_card = deck.deal()
	print dealt_card
	dealer.add_card_to_hand(dealt_card)
dealer.display_hand(hidden=True)
dealer.display_hand(hidden=False)
print dealer.get_hand_value()

#test Aces
player.hand_values = [10,10,1,1]
print player.get_hand_value()
player.hand_values = [10,1]
print player.get_hand_value()
player.hand_values = [5,5,1]
print player.get_hand_value()

#test Blackjack
player.hand_values = [10,1]
print player.get_hand_value()
print player.has_blackjack()


