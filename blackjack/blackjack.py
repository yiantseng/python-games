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

	#Print welcome header
	print 50*'-'
	print 'Welcome to Blackjack!'
	print 'Blackjack Pays 3:2'
	print 50*'-'

	#Play the game while chip stack is not empty
	while player.get_chip_stack()>0:	
		
		#Shuffles the deck if necessary
		deck.shuffle()

		#Ask for the player's bet
		print 	
		bet = int(player.bet())
		print

		#Initial deal of two cards to each player
		for i in range(1,3):
			player.add_card_to_hand(deck.deal())
			dealer.add_card_to_hand(deck.deal())

		#Check if player or dealer has a blackjack	
		if player.has_blackjack() or dealer.has_blackjack():
			#Display hands with the dealer's card hidden
			player.display_hand()
			dealer.display_hand(hidden = True)

			#Special blackjack cases
			result = moderator.determine_blackjack_result()

			#Add appropriate chips
			if result == 'insurance':
				player.add_chips(bet)
				player.chip_stack -= int(round(bet/2))
			elif result == 'push':
				player.add_chips(bet)
			elif result == 'blackjack':
				player.add_chips(int(bet + bet * 1.5))

			player.reset_hand()
			dealer.reset_hand()	
		#Otherwise continue normally		
		else:
			#Display hands with the dealer's card hidden
			player.display_hand()
			dealer.display_hand(hidden = True)
			
			#Takes insurance only if player buys insurance
			if dealer.ask_for_insurance():
				player.chip_stack -= int(round(bet/2))
			#Give player the option to double down if initial hand equals 9, 10, or 11
			if player.double_down():
				player.chip_stack -= bet
				bet = bet * 2
				player.add_card_to_hand(deck.deal())
			#Ask player to hit or stand, while their hand has not busted
			else:
				moderator.determine_hit_or_stand()
				'''	
				while player.get_hand_score() <= 21:
					print
					ask_player = raw_input('Hit(h) or Stand(s)?')
					if ask_player == 'h':
						player.add_card_to_hand(deck.deal())
						#print new hand only if it is not a bust
						if player.get_hand_score() <= 21:
							player.display_hand() 				
					elif ask_player == 's':
						break
					else:
						print "Not a valid move. Please press (h) or (s)"	
				'''
			#Deal cards to dealer, dealer can only stop at a soft 17 or higher		 
			while dealer.get_hand_score() < 17:
				dealer.add_card_to_hand(deck.deal())
					
			#Display resulting hands and points, as well as revealing the dealer's hand
			player.display_hand()
			dealer.display_hand(hidden=False)
			

			#Results are determined and appropriate chips distributed
			result = moderator.determine_result()
			if result == 'win':
				player.add_chips(bet * 2)
			elif result == 'push':	
				player.add_chips(bet)
			
			#Clears hands
			player.reset_hand()
			dealer.reset_hand()

	print 'No more chips. Better luck next time!'

if __name__ == "__main__":
    main()