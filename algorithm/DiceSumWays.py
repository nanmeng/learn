class Stack(object):
	def __init__(self):
		self.data = []

	def push(self, value):
		self.data.append(value)

	def pop(self):
		top = len(self.data) - 1
		if top >= 0:
			ret = self.data[top]
			del self.data[-1]
			return ret
		else:
			return None

	def peek(self):
		top = len(self.data) - 1
		if top >= 0:
			return self.data[top]
		else:
			return None

	def emptify(self):
		while self.pop():
			pass

	def toString(self):
		for i in xrange(0, len(self.data)):
			print self.data[i],
		print

tried = Stack()

def howDicesMakeOutcome(dices, outcome, index):
	# see how the given dices can make up
	# to the given outcome, trying from the
	# dice at the given index
	# dices would be an array of arrays
	# each child array represents a dice
	if len(dices) <= 0:
		print 'NOPE', tried.toString()
		return False
	if index >= len(dices):
		print 'NOPE', tried.toString()
		return False
	# use the dice at given index
	dice = dices[index]
	# assume dices all have at least one
	# possible outcome (face)
	for i in xrange(0, len(dice)):
		# print 'trying face:', dice[i], 'from dice:', index
		tried.push(str(index) + ':' + str(dice[i]))

		if index == len(dices)-1:
			# if this is the last we try
			if dice[i] == outcome:
				# if this face equals to outcome
				print 'YES ', tried.toString()
				tried.pop()
			elif i == len(dice)-1:
				# if this is the last face we try
				print 'NOPE', tried.toString()
				tried.pop()
				return
			else:
				tried.pop()
		else:
			howDicesMakeOutcome(dices, outcome-dice[i], index+1)
			tried.pop()

if __name__ == '__main__':
	dices = [
		[1,2,3,4],
		[1,2,3,4,5],
		[1],
		[4],
		[3,6,9,12],
			]
	howDicesMakeOutcome(dices, 10, 0)
	print '--------'
	howDicesMakeOutcome(dices, 20, 0)
