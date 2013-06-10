class Queue(object):
	def __init__(self, size):
		self.data = []
		self.size = size
		for i in xrange(0, size):
			self.data.append(None)
		self.head = 0
		self.tail = 0
	
	def enqueue(self, value):
		if self.tail == self.head and self.data[self.head]:
			print 'full'
			return
		self.data[self.tail] = value
		self.tail += 1
		if self.tail >= self.size:
			self.tail = 0

	def dequeue(self):
		if self.head == self.tail and not self.data[self.head]:
			print 'empty'
			return
		ret = self.data[self.head]
		self.data[self.head] = None
		self.head += 1
		if self.head >= self.size:
			self.head = 0
		return ret

	def toString(self):
		print 'head:', self.head, 'tail:', self.tail, 'data:', self.data

if __name__ == '__main__':
	A = [1,2,3,4,5,6,7,8,9]
	Q = Queue(10)
	for i in xrange(0, len(A)):
		Q.enqueue(A[i])
		Q.toString()
	for i in xrange(0, len(A)):
		print Q.dequeue()
		Q.toString()

