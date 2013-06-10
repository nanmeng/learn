# TODO this does not work
class Deque(object):
	def __init__(self, size):
		self.data = []
		self.size = size
		for i in xrange(0, size):
			self.data[i] = None
		self.head = 0
		self.tail = 0

	def enqueHead(self, value):
		if self.head == self.tail and self.data[self.tail]:
			print 'full'
			return
		self.data[self.tail] = value
		self.tail += 1
		if self.tail >= self.size:
			self.tail = 0

	def enqueTail(self, value):
		if self.tail == self.head and self.data
		pass

	def dequeHead(self, value):
		pass

	def dequeTail(self, value):
		pass
