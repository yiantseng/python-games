class Player:
	def __init__(self):
		'''initialize hand values/score and display as arrays'''
		self.hand_values = []
		self.hand_display = []
		self.hand_score = 0

	#adds the card dealt to the hand, separating the card display and value for processing
	def add_card_to_hand(self,card):
		self.hand_display.append(card[0])
		self.hand_values.append(card[1])
		#pushes aces to the end so that their values can be evaluated last
		for card in self.hand_values:
			if card == 1:
				index = self.hand_values.index(card)
				self.hand_values.append(self.hand_values.pop(index))

	#Loops through the hand and adds up the value of each card
	def get_hand_score(self):
		self.hand_score=0
		for card in self.hand_values:
			#Checks if ace should be 1 or 11
			if card == 1 and self.hand_score + 11 <= 21:
				self.hand_score += 11	
			else:
				self.hand_score += card	
		return self.hand_score

	def has_blackjack(self):
		#if hand is only two cards and is scored a 21, then the hand is a blackjack
		self.get_hand_score()
		if self.hand_score == 21 and len(self.hand_values) == 2:
			return True		
		else:
			return False	
	
	def display_hand(self):
		print
		print 'Your hand:' 
		print self.hand_display
		print "Your hand is at " + str(self.get_hand_score()) + " points."
		print
	
	def reset_hand(self):
		self.hand_values = []
		self.hand_display = []

	def ask_for_special_hand(self,hand_type):
		while True:	
			try:
				response = raw_input("Do you want to %s? ( y ) or ( n ): " % hand_type)	
				if response == 'y':
					return True
				elif response == 'n':
					return False		
				else:
					print "Please type ( y ) or ( n )"
			except ValueError:
				print "Please type ( y ) or ( n )"


class BlackJackDealer(Player):
	#dealer hand can be hidden from player's view
	def display_hand(self,hidden):
	    print
	    print 'Dealer hand:'
	    if hidden:
			print self.hand_display[1:len(self.hand_display)]
	    else:
			print self.hand_display
			print "Dealer hand is at " + str(self.get_hand_score()) + " points."
			print	

	def ask_for_insurance(self):
		if 'Ace' in self.hand_display[1]:
			return self.ask_for_special_hand('pay insurance')			
		else:
			return False	

class BlackJackPlayer(Player):	
	def __init__(self):
		'''initialize include a chip stack for the blackjack player'''
		self.chip_stack = 100
		self.hand_values = []
		self.hand_display = []
		self.hand_score = 0

	#asks player for their bet and checks if the bet is valid
	#subtracts chips from stack and returns the bet	
	def bet(self):
		while True:
			try:
				bet = raw_input("How much do you want to bet? ")	
				if int(bet) < 1:
					print "Please bet at least one chip to play."
				elif int(bet) > self.chip_stack:
					print "You only have " + str(self.chip_stack) + " chips."
				else:
					break				
			except ValueError:
				print "That is not a valid number."
		self.chip_stack-=int(bet)
		return bet

	def double_down(self):
		if self.hand_score in [9,10,11]:
			return self.ask_for_special_hand('double down')		
		else:
			return False

 	def add_chips(self,amount):
 		self.chip_stack += amount

	def get_chip_stack(self):
		print
		print "You have this many chips remaining:"
		print self.chip_stack
		return self.chip_stack	