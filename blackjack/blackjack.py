from deck import Deck
from players import Player, BlackJackDealer, BlackJackPlayer



def main():
	dealer=BlackJackDealer()
	player=BlackJackPlayer()
	deck=Deck()
	deck.load_deck()

	while player.get_chip_stack()>0:	
		
		if deck.cards_in_deck<10:
			deck.clear_deck()
			deck.load_deck()

		print "You have this many chips remaining:"
		print player.get_chip_stack()
		bet=int(player.bet())

		#initial deal of two cards to each player
		for i in range(1,3):
			player.add_card_to_hand(deck.deal())
			dealer.add_card_to_hand(deck.deal())

		#display hands, with the first dealer card hidden
		player.display_hand()
		print "Your hand is at " + str(player.get_hand_value()) + " points."
		dealer.display_hand(hidden=True)

		#ask player to hit or stand
		while True:
			ask_player=raw_input('Hit(h) or Stand(s)?')
			if ask_player=='h':
				player.add_card_to_hand(deck.deal())
				print "Your hand is at " + str(player.get_hand_value()) + " points."
			else:
				 break
		#deal cards to dealer, dealer can only stop at a soft 17 or higher		 
		while dealer.get_hand_value()<17:
			dealer.add_card_to_hand(deck.deal())
				
		#display resulting hands and points, revealing the dealer's hand
		player.display_hand()
		print "Your hand is at " + str(player.get_hand_value()) + " points."
		dealer.display_hand(hidden=False)
		print "Dealer hand is at " + str(dealer.get_hand_value()) + " points."

		dealer_hand=dealer.get_hand_value()
		player_hand=player.get_hand_value()

		#clears hands
		player.reset_hand()
		dealer.reset_hand()	

		#see who wins

		if player_hand>dealer_hand and player_hand<21 or dealer_hand>21:
			print "You win!"
			player.add_chips(bet)
			player.add_chips(bet)
		elif player_hand>21:
			print "Bust!"		
		elif dealer_hand==player_hand:
			print "Push!"
			player.add_chips(bet)		
		elif dealer_hand>player_hand and dealer_hand<21:
			print "You lose!"
		else:
			print "You lose!"						

if __name__ == "__main__":
    main()