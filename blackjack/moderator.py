from deck import Deck
from players import Player, BlackJackDealer, BlackJackPlayer

class Moderator():
	def __init__(self,BlackJackPlayer,BlackJackDealer,Deck):
		self.player=BlackJackPlayer
		self.dealer=BlackJackDealer
		self.deck=Deck

	def determine_blackjack_result(self):
		if self.player.has_blackjack()==self.dealer.has_blackjack():
			print
			print "Push!"
			self.player.add_chips(bet)
			return 'push'	
		elif self.player.has_blackjack():
			print
			self.player.display_hand()
			print "You hit a blackjack!"
			self.player.reset_hand()
			self.dealer.reset_hand()
			return 'blackjack'
		else:
			print
			self.dealer.display_hand(hidden=False)
			print "Dealer hit a blackjack!"

	#determines the result and resets hands		
	def determine_result(self):
		#variables to keep track of final values
		dealer_hand=self.dealer.get_hand_value()
		player_hand=self.player.get_hand_value()

		#clears hands
		self.player.reset_hand()
		self.dealer.reset_hand()	

		#determine the outcomes and add chips where appropriate
		if (player_hand>dealer_hand or dealer_hand>21) and player_hand<=21:
			print "You win!"
			return 'win'
		elif player_hand>21:
			print "Bust!"
			if dealer_hand>21:
				print "Shouldn't have hit, the dealer busted also!"		
		elif dealer_hand==player_hand:
			print "Push!"
			return 'push'		
		elif dealer_hand>player_hand and dealer_hand<=21:
			print "You lose!"
		else:
			print "You lose!"