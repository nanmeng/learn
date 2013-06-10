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

	def toString(self):
		for i in xrange(0, len(self.data)):
			print self.data[i],
		print

class Node(object):
	def __init__(self, left, right, height):
		self.height = height
		self.left = left
		self.right = right
	def toString(self):
		print '(', self.height, 'L:',
		if self.left != '0':
			self.left.toString()
		else:
			print self.left,
		print 'R:',
		if self.right != '0':
			self.right.toString()
		else:
			print self.right,
		print ')'

def getTreeHeightForString(S):
	# turn the string into list (array)
	S = list(S)
	print S
	if len(S) <= 0:
		# nothing in array
		return None
	# we need a stack for the parens
	parens = Stack()
	# we need a stack for the nodes
	nodes = Stack()
	# start traversing the array
	i = 0
	max_height = float('-inf')
	while i < len(S):
		print 'parens:', parens.toString()
		print 'nodes:', nodes.toString()
		if S[i] == '(':
			parens.push(S[i])
		elif S[i] == '0':
			nodes.push(S[i])
		elif S[i] == ')':
			# process
			height = 0
			try:
				right = nodes.pop()
				left = nodes.pop()

				if left != '0':
					left.toString()
				if right != '0':
					right.toString()

				if left != '0':
					height = left.height
				if right != '0' and right.height > height:
					height = right.height
				# we need a matching left paren
				left_paren = parens.pop()
				height += 1
			except:
				print 'invalid string'
				return
			# construct a new node with left and right children
			node = Node(left, right, height)
			node.toString()
			if height > max_height:
				max_height = height
			# push new node to the nodes stack
			nodes.push(node)
		else:
			print 'invalid char'
			return
		i += 1
	return max_height

if __name__ == '__main__':
	S = [
			'(00)',
			'((00)0)',
			'((00)(00))',
			'((00)(0(00)))',
			'((00)(0(0(00))))',
			'x',
			'0',
			'()',
			'(0)',
			'(00)x',
			'(0p)',
			]
	for s in S:
		print '------------'
		print getTreeHeightForString(s)
