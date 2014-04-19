from deck import Deck
from players import Player, BlackJackDealer, BlackJackPlayer
from moderator import Moderator

def main():

	#Create players,deck, and moderator
	dealer = BlackJackDealer()
	player = BlackJackPlayer()
	deck = Deck()
	deck.load_deck()
	moderator = Moderator(player,dealer,deck)

	print 50*'-'
	print 'Welcome to Blackjack!'
	print 'Blackjack Pays 3:2'
	print 50*'-'

	#Play the game while chip stack is not empty
	while player.get_chip_stack()>0:	
		
		#Shuffles the deck if necessary
		deck.shuffle()

		print
		print "You have this many chips remaining:"
		print player.get_chip_stack()

		print 	
		bet = int(player.bet())

		#Initial deal of two cards to each player
		for i in range(1,3):
			player.add_card_to_hand(deck.deal())
			dealer.add_card_to_hand(deck.deal())

		#Check if player or dealer has a blackjack	
		if player.has_blackjack() or dealer.has_blackjack():
			#Special blackjack cases
			result = moderator.determine_blackjack_result()
			if result == 'push':
				player.add_chips(bet)
			elif result == 'blackjack':
				player.add_chips(int(bet + bet * 1.5))
		#Otherwise continue normally		
		else:
			#Display hands with the dealer's card hidden
			print 
			player.display_hand()
			print "Your hand is at " + str(player.get_hand_value()) + " points."
			print 
			dealer.display_hand(hidden = True)
			
			#Ask player to hit or stand, while their hand has not busted
			while player.get_hand_value() <= 21:
				print
				ask_player = raw_input('Hit(h) or Stand(s)?')
				if ask_player == 'h':
					player.add_card_to_hand(deck.deal())
					#print new hand only if it is not a bust
					if player.get_hand_value() <= 21:
						player.display_hand()
						print "Your hand is at " + str(player.get_hand_value()) + " points."
						print 				
				elif ask_player == 's':
					break
				else:
					print "Not a valid move. Please press (h) or (s)"	
				
			#deal cards to dealer, dealer can only stop at a soft 17 or higher		 
			while dealer.get_hand_value() < 17:
				dealer.add_card_to_hand(deck.deal())
					
			#display resulting hands and points, as well as revealing the dealer's hand

			player.display_hand()
			print "Your hand is at " + str(player.get_hand_value()) + " points."
			dealer.display_hand(hidden=False)
			print "Dealer hand is at " + str(dealer.get_hand_value()) + " points."

			#results determined and appropriate chips distributed
			result = moderator.determine_result()
			if result == 'win':
				player.add_chips(bet * 2)
			elif result == 'push':	
				player.add_chips(bet)
			

	print 'No more chips. Better luck next time!'

if __name__ == "__main__":
    main()