import random
import unittest
from deck import Deck
from players import Player, BlackJackDealer, BlackJackPlayer


class BlackJackTest:

	dealer=BlackJackDealer()
	player=BlackJackPlayer()
	deck=Deck()
	
	deck.load_deck()
	for card in range(0,deck.cards_in_deck):
		print card
		print deck.deal()
		print deck.index
		print deck.cards_in_deck
		print deck.deck

		

	#player
	def checkDealing(self):
		deck.deal()

	def testAces(self):
		player_hand=[10,10,1]
		hand_value(dealer_hand)
		hand_value(player_hand)