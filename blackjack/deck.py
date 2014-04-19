import random


class Deck():
	def __init__(self):
		'''initialize deck, number of cards in deck, and card values'''
		self.deck=[]
		self.cards_in_deck=0
		self.faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
		self.values=[1,2,3,4,5,6,7,8,9,10,10,10,10]
		self.suits= ['Spades', 'Clubs' , 'Diamonds','Hearts']
			

	#loads the deck with cards
	def load_deck(self):
		for card in range(0,52):
			self.deck.append(card)
			self.cards_in_deck+=1

	def clear_deck(self):
		self.deck=[]
		self.cards_in_deck=0		

	#shuffle when there are less than 15 cards	
	def shuffle(self):
		if self.cards_in_deck<15:
			self.clear_deck()
			self.load_deck()
			

	#deals a random card from the deck, then stores the card display and value in an array
	def deal(self):
		self.cards_in_deck-=1
		self.index=random.randint(0,self.cards_in_deck-1)
		card=self.deck.pop(self.index)
		dealt_card=[self.faces[card%13]+' of '+self.suits[card/13],self.values[card%13]]
		return dealt_card					
