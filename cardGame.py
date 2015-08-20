class Card :
	letter = None
	number = None
	def __init__(self, letter, number):
		self.letter = letter
		self.number = number

# init
letter = ['A' , 'B', 'C', 'D', 'E']
card = []
for i in letter:
	for j in range(1, 10):
		card.append(Card(i, j))

for i in card:
	print i.letter, i.number, " "

def game(card):
	window = []
	for i in range(len(card)):
		#set up a loop for getting card form your hand
		window.append(card[i])
		if(len(window) == 4):
			if(checkLose(window)):
				print "lose"
				return False
			else: 
				pass
	if(len(window) == 0):
		print "win"
		return True
	else: 
		print "lose"
		return False
