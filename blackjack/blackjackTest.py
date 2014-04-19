from deck import Deck
from players import Player, BlackJackDealer, BlackJackPlayer

dealer = BlackJackDealer()
player = BlackJackPlayer()
deck = Deck()

#test Deck Class
deck.load_deck()
for card in range(0,deck.cards_in_deck-1):
	print card
	print deck.deal()
	print deck.index
	print deck.cards_in_deck
	print deck.deck	
deck.shuffle()	
print deck.deck

#test Player Class

for card in range(0,4):
	dealt_card = deck.deal()
	print dealt_card
	player.add_card_to_hand(dealt_card)
player.display_hand()
print player.get_hand_score()

#test Dealer
deck.load_deck()
for card in range(0,2):
	dealt_card = deck.deal()
	print dealt_card
	dealer.add_card_to_hand(dealt_card)
dealer.display_hand(hidden=True)
dealer.display_hand(hidden=False)
print dealer.get_hand_score()


#test Aces
player.hand_values = [10,10,1,1]
print player.get_hand_score()
player.hand_values = [10,1]
print player.get_hand_score()
player.hand_values = [5,5,1]
print player.get_hand_score()

#test Blackjack
player.hand_values = [10,1]
print player.get_hand_score()
print player.has_blackjack()

#test insurance
dealer.hand_values = [10,1]
dealer.hand_display = ['Queen of Spades','Ace of Spades']
dealer.display_hand(hidden=True)
print dealer.ask_for_insurance()
print
dealer.hand_values = [1,10]
dealer.hand_display = ['Ace of Spades','Queen of Spades']
dealer.display_hand(hidden=True)

print dealer.ask_for_insurance()

#test double down
print
player.hand_values = [9,2]
player.get_hand_score()
print player.double_down()

