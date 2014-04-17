class Player:
	def __init__(self):
		self.hand_values=[]
		self.hand_display=[]

	#adds the card dealt to the hand, separating the card display and value for processing
	def add_card_to_hand(self,card):
		self.hand_display.append(card[0])
		self.hand_values.append(card[1])
		#pushes aces to the end so that their values can be evaluated last
		for card in self.hand_values:
			if card==1:
				index=self.hand_values.index(card)
				self.hand_values.append(self.hand_values.pop(index))

	#loops through the hand and adds up the value of each card
	def get_hand_value(self):
		hand_value=0

		for card in self.hand_values:
			#checks if ace should be 1 or 11
			if card == 1 and hand_value+11<=21:
				hand_value+=11	
			else:
				hand_value+=card	
		return hand_value
	
	def display_hand(self):
		print self.hand_display
	
	def reset_hand(self):
		self.hand_values=[]
		self.hand_display=[]

class BlackJackDealer(Player):
	def display_hand(self,hidden):
		if hidden:
			print self.hand_display[1:len(self.hand_display)]
		else:	
			print self.hand_display

class BlackJackPlayer(Player):	
	def __init__(self):
		self.chip_stack=100
		self.hand_values=[]
		self.hand_display=[]

	#asks player for their bet, check if bet is valid	
	def bet(self):
		bet= raw_input("How much do you want do bet? ")
		
		while True:
			try:
				if int(bet)<1 or int(bet)>self.chip_stack:
					print "Invalid chip number"
					bet= raw_input("How much do you want do bet? ")	
				break
			except ValueError:
				print "That is not a number."
				bet= raw_input("How much do you want do bet? ")		
		
		self.chip_stack-=int(bet)		
 
	def get_chip_stack(self):
		return self.chip_stack	