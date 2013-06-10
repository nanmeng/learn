class Key(object):
	def __init__(self, value):
		self.value = value
		v = ord(value) - ord('a')
		self.x = v / 5
		self.y = v % 5
	
	def toString(self):
		print self.value, '(', self.x, ',', self.y, ')'

def HMove(pos, key):
	hMove = key.y - pos[0]
	if hMove > 0:
		# right
		if pos[1] == 5:
			return False
		pos[0] += 1
		print '>',
	elif hMove < 0:
		# left
		pos[0] -= 1
		print '<',

def VMove(pos, key):
	vMove = key.x - pos[1]
	if vMove > 0:
		# down
		if pos[1] == 4 and pos[0] > 0:
			return False
		pos[1] += 1
		print 'v',
	elif vMove < 0:
		# up
		pos[1] -= 1
		print '^',

def onScreenKeyboard(S):
	print '======='
	pos = [0, 0]
	S = list(S)
	for c in S:
		key = Key(c)
		# print '(', pos[0], ',', pos[1], ') ->',
		# key.toString()
		while not (pos[0] == key.y and pos[1] == key.x):
			HMove(pos, key)
			VMove(pos, key)
		print '!', key.value
	print


if __name__ == '__main__':
	S = ''
	onScreenKeyboard(S)
	S = 'a'
	onScreenKeyboard(S)
	S = 'abcdefghbqrzyzeptz'
	# S = 'ab'
	onScreenKeyboard(S)
