from deck import Deck
from players import Player, BlackJackDealer, BlackJackPlayer

def main():
	dealer=BlackJackDealer()
	player=BlackJackPlayer()
	deck=Deck()
	deck.load_deck()

	print 50*'-'
	print 'Welcome to BlackJack!'
	print 50*'-'

	#play the game while chip stack is not empty
	while player.get_chip_stack()>0:	
		
		#shuffles the deck if necessary
		deck.shuffle()

		print
		print "You have this many chips remaining:"
		print player.get_chip_stack()

		print 	
		bet=int(player.bet())

		#initial deal of two cards to each player
		for i in range(1,3):
			player.add_card_to_hand(deck.deal())
			dealer.add_card_to_hand(deck.deal())

		#display hands, with the first dealer card hidden
		print 
		player.display_hand()
		print "Your hand is at " + str(player.get_hand_value()) + " points."
		print 
		dealer.display_hand(hidden=True)

		#ask player to hit or stand, while their hand has not busted
		while player.get_hand_value()<21:
			print
			ask_player=raw_input('Hit(h) or Stand(s)?')
			if ask_player=='h':
				player.add_card_to_hand(deck.deal())
				#print new hand only if it is not a bust
				if player.get_hand_value()<21:
					player.display_hand()
					print "Your hand is at " + str(player.get_hand_value()) + " points."
					print 				
			else:
				break
				
		#deal cards to dealer, dealer can only stop at a soft 17 or higher		 
		while dealer.get_hand_value()<17:
			dealer.add_card_to_hand(deck.deal())
				
		#display resulting hands and points, revealing the dealer's hand
		print
		player.display_hand()
		print "Your hand is at " + str(player.get_hand_value()) + " points."
		print
		dealer.display_hand(hidden=False)
		print "Dealer hand is at " + str(dealer.get_hand_value()) + " points."

		dealer_hand=dealer.get_hand_value()
		player_hand=player.get_hand_value()
		print

		#clears hands
		player.reset_hand()
		dealer.reset_hand()	

		#determine the outcomes
		if (player_hand>dealer_hand or dealer_hand>21) and player_hand<=21:
			print "You win!"
			player.add_chips(bet*2)
		elif player_hand>21:
			print "Bust!"		
		elif dealer_hand==player_hand:
			print "Push!"
			player.add_chips(bet)		
		elif dealer_hand>player_hand and dealer_hand<=21:
			print "You lose!"
		else:
			print "You lose!"					

	print 'No more chips. Better luck next time!'
			
if __name__ == "__main__":
    main()