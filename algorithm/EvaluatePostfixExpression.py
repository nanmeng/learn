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
			print self.data[i]

class Queue(object):
	def __init__(self, size):
		self.size = size
		self.store = []
		for i in xrange(0, size):
			self.store.append(None)
		self.head = 0
		self.tail = 0
	
	def EQ(self, value):
		self.toString()
		print 'EQ:',
		if self.store[self.tail] is not None:
			raise Exception('full')
		else:
			self.store[self.tail] = value
			self.tail = (self.tail + 1) % self.size
		self.toString()

	def DQ(self):
		self.toString()
		print 'DQ:',
		if self.store[self.head] is None:
			raise Exception('empty')
		else:
			ret = self.store[self.head]
			self.store[self.head] = None
			self.head = (self.head + 1) % self.size
		self.toString()
		return ret

	def toString(self):
		print 'head:', self.head, 'tail:', self.tail, 'store:', self.store

def evaluatePostfixExpression(E):
	s = Stack()
	for x in E:
		print x
		if x.isdigit():
			s.push(int(x))
		else:
			R = s.pop()
			L = s.pop()
			v = 0
			if x == '+':
				v = L + R
			elif x == '-':
				v = L - R
			elif x == '*':
				v = L * R
			elif x == '/':
				v = L / R
			else:
				raise Exception('invalid char')
			s.push(v)
	print s.pop()

if __name__ == '__main__':
	E = list('12*84/+5-67*+')
	evaluatePostfixExpression(E)
