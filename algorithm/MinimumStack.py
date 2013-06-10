class MinStack(object):
	def __init__(self):
		self.stack = Stack()
		self.minStack = Stack()

	def push(self, value):
		Min = self.minStack.peek()
		if not Min or value <= Min:
			self.minStack.push(value)
		self.stack.push(value)

	def pop(self):
		Min = self.minStack.peek()
		top = self.stack.pop()
		if Min == top:
			self.minStack.pop()
		return top

	def getMin(self):
		return self.minStack.peek()

	def toString(self):
		print "stack:"
		self.stack.toString()
		print "minStack:"
		self.minStack.toString()

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

if __name__ == '__main__':
	s = MinStack()
	print s.toString()

	print '---'
	s.push(3)
	print s.toString()

	print '---'
	s.push(1)
	s.push(1)
	s.push(1)
	print s.toString()

	print '---'
	s.push(5)
	print s.toString()


	print '---'
	s.push(7)
	s.push(7)
	s.push(7)
	s.push(7)
	print s.toString()

	print '---'
	s.push(0)
	s.push(0)
	print s.toString()

	print '---'
	s.pop()
	print s.toString()

	print '---'
	s.pop()
	print s.toString()
	print '---'
	s.pop()
	print s.toString()
	print '---'
	s.pop()
	print s.toString()
	print '---'
	s.pop()
	print s.toString()
