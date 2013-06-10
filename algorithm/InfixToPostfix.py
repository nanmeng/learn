class Stack(object):
	def __init__(self):
		self.data = []
		self.top = -1

	def push(self, item):
		if (self.top+1) == len(self.data):
			self.data.append(item)
		else:
			self.data[self.top] = item
		self.top += 1

	def pop(self):
		if self.top < 0:
			return None
		top = self.data[self.top]
		del self.data[self.top]
		self.top -= 1
		return top

	def peek(self):
		if self.top < 0:
			return None
		return self.data[self.top]

	def toString(self):
		print '>>>'
		print 'top:', self.top
		i = self.top
		while i >= 0:
			d = self.data[i]
			# print d.__class__.__name__
			if d.__class__.__name__ == 'Node':
				d.toString()
			else:
				print d
			i -= 1
		print '<<<'

class Node(object):
	def __init__(self, i, value, left=None, right=None):
		self.i = i
		self.value = value
		self.left = left
		self.right = right

	def toString(self):
		print '[', self.i, '-', self.value,
		print 'L:',
		if self.left.__class__.__name__ == 'Node':
			print self.left.i,
		else:
			print self.left,
		print 'R:',
		if self.right.__class__.__name__ == 'Node':
			print self.right.i,
		else:
			print self.right,
		print ']'

def isOp(s):
	# check if s is an operator
	if s in ['+','-','*','/']:
		return True
	return False

def infixToPostfix(S):
	# convert infix expression to postfix expression
	i = 0
	node_i = 0
	v = Stack()
	op = Stack()
	while i < len(S):
		value = ''
		print 'S[',i,']',S[i]
		if S[i] == '(':
			# prepend all ('s
			n = i
			while n < len(S):
				if S[n] == '(':
					value += S[n]
				else:
					break
				n += 1
				i += 1
			if n >= len(S):
				print 'invalid'
				return
			value += S[n]
			node = Node(node_i, value)
			print node_i, 'pushing:',
			node.toString()
			node_i += 1
			v.push(node)
			i += 1
		elif isOp(S[i]):
			op.push(S[i])
			print 'pushing operator:', S[i]
			i += 1
		else:
			if S[i] == ')':
				print 'invalid'
				return
			value = S[i]
			n = i+1
			has_right_paren = False
			while n < len(S):
				# append all following )'s
				if S[n] == ')':
					has_right_paren = True
					value += S[n]
				else:
					break
				n += 1
				i += 1
			node = Node(node_i, value)
			print node_i, 'newnode:',
			node.toString()
			node_i += 1
			if has_right_paren:
				operator = op.pop()
				right = node
				left  = v.pop()
				node = Node(node_i, operator, left, right)
				node_i += 1
			print node_i-1, 'pushing:',
			node.toString()
			v.push(node)
			i += 1
		v.toString()
		op.toString()

	print '--------'
	while op.peek():
		try:
			right = v.pop()
			left  = v.pop()
			operator = op.pop()
			node = Node(node_i, operator, left, right)
			node_i += 1
			print node_i-1, 'pushing:',
			node.toString()
			v.push(node)
		except:
			print 'invalid'
			return
		v.toString()
		op.toString()
	return v.pop()

if __name__ == '__main__':
	S = '(((1+2)*3+4*(5-6))/7+8)*9'
	node = infixToPostfix(S)
	node.toString()
