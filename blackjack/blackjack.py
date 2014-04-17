from deck import Deck
from players import Player, BlackJackDealer, BlackJackPlayer



def main():
	dealer=BlackJackDealer()
	player=BlackJackPlayer()
	deck=Deck()

	while player.get_chip_stack()>0:	
		deck.load_deck()
		player.bet()

		for i in range(1,3):
			player.add_card_to_hand(deck.deal())
			dealer.add_card_to_hand(deck.deal())

		
		print 'Your hand:' 	
		player.display_hand()
		print "Your hand is at " + str(player.get_hand_value()) + " points."
		print 'Dealer hand:'
		dealer.display_hand(hidden=True)

		while True:
			ask_player=raw_input('Hit(h) or Stand(s)?')
			if ask_player=='h':
				player.add_card_to_hand(deck.deal())
				print "Your hand is at " + str(player.get_hand_value()) + " points."
			else:
				 break

		while dealer.get_hand_value()<17:
			dealer.add_card_to_hand(deck.deal())
				
		dealer_hand=dealer.get_hand_value()	
		player_hand=player.get_hand_value()

		print 'Your hand:' 	
		player.display_hand()
		print "Your hand is at " + str(player.get_hand_value()) + " points."
		print 'Dealer hand:'
		dealer.display_hand(hidden=False)
		print "Dealer hand is at " + str(dealer.get_hand_value()) + " points."

		print player.get_chip_stack()
		
		player.reset_hand()
		dealer.reset_hand()	
		
		if dealer_hand<=21:
			if player_hand>dealer_hand:
				print "You win!"
			else:
				print "You lose!"
		elif player_hand>dealer_hand or dealer_hand>21:
			print "You win!"
		else:
			print "You lose!"						

if __name__ == "__main__":
    main()