from deck import Deck
from players import Player, BlackJackDealer, BlackJackPlayer

class Moderator():
	def __init__(self,BlackJackPlayer,BlackJackDealer,Deck):
		self.player = BlackJackPlayer
		self.dealer = BlackJackDealer
		self.deck = Deck

	def determine_blackjack_result(self):
		if self.player.has_blackjack() and self.dealer.has_blackjack():
			print
			print "Push!"
			return 'push'	
		elif self.player.has_blackjack():
			print
			print "You hit a blackjack!"
			return 'blackjack'
		else:
			if self.dealer.ask_for_insurance():
				return 'insurance'
			self.player.display_hand()
			self.dealer.display_hand(hidden = False)
			print "Dealer hit a blackjack!"

	def determine_hit_or_stand(self):
		while self.player.get_hand_score() <= 21:
			print
			ask_player = raw_input('Hit(h) or Stand(s)?')
			if ask_player == 'h':
				self.player.add_card_to_hand(self.deck.deal())
				#print new hand only if it is not a bust
				if self.player.get_hand_score() <= 21:
					self.player.display_hand() 				
			elif ask_player == 's':
				break
			else:
				print "Not a valid move. Please press (h) or (s)"

	#Determines the result and resets hands		
	def determine_result(self):
		#Variables to keep track of final hand scores
		dealer_hand = self.dealer.get_hand_score()
		player_hand = self.player.get_hand_score()
		dealer_bust = dealer_hand > 21

		#Determine the outcomes and add chips where appropriate
		if (player_hand > dealer_hand or dealer_bust) and player_hand <= 21:
			if dealer_bust:
				print "Dealer Busted!"
			print "You win!"
			return 'win'
		elif player_hand > 21:
			print "Bust!"
			if dealer_bust:
				print "Shouldn't have hit, the dealer busted also!"		
		elif dealer_hand == player_hand:
			print "Push!"
			return 'push'		
		elif dealer_hand > player_hand and dealer_hand <= 21:
			print "You lose!"
		else:
			print "You lose!"

