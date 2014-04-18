import random


class Deck():
	def __init__(self):
		self.deck=[]
		self.faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
		self.values=[1,2,3,4,5,6,7,8,9,10,10,10,10]
		self.suits= ['Spades', 'Clubs' , 'Diamonds','Hearts']
		self.cards_in_deck=52

	#loads the deck with cards
	def load_deck(self):
		for card in range(0,52):
			self.deck.append(card)

	def clear_deck(self):
		self.deck=[]		

	def shuffle(self):
		if self.cards_in_deck<10:
			self.load_deck()
			self.clear_deck()

	#deals a random card from the deck
	def deal(self):
		self.cards_in_deck-=1
		self.index=random.randint(0,self.cards_in_deck)
		card=self.deck.pop(self.index)
		#stores the card display and card value in an array
		dealt_card=[self.faces[card%13]+' of '+self.suits[card/13],self.values[card%13]]
		
		return dealt_card					
