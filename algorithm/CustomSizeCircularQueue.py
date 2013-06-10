class CircularQueue(object):
	def __init__(self, size):
		if size <= 0:
			raise Exception('queue size must > 0')
		self.data = []
		self.size = size
		for i in xrange(0, size):
			self.data.append(None)
		self.h = 0
		self.t = 0
	def enqueue(self, value):
		if self.data[self.t] is None:
			self.data[self.t] = value
			self.t = (self.t+1) % self.size
		else:
			print 'full'
			return
	def dequeue(self):
		if self.data[self.h] is None:
			print 'empty'
			return
		else:
			ret = self.data[self.h]
			self.data[self.h] = None
			self.h = (self.h+1) % self.size
	def toString(self):
		print 'h:',self.h,
		print 't:',self.t,
		print 's:',self.size,
		print self.data

if __name__ == '__main__':
	A = list('1234567890')
	Q = CircularQueue(5)

	print '-------'
	for i in xrange(0, len(A)):
		Q.toString()
		Q.enqueue(A[i])
	for i in xrange(0, len(A)):
		Q.toString()
		Q.dequeue()

	Q = CircularQueue(10)
	print '-------'
	for i in xrange(0, len(A)):
		Q.toString()
		Q.enqueue(A[i])
	for i in xrange(0, len(A)):
		Q.toString()
		Q.dequeue()

	Q = CircularQueue(15)
	print '-------'
	for i in xrange(0, len(A)):
		Q.toString()
		Q.enqueue(A[i])
	for i in xrange(0, len(A)):
		Q.toString()
		Q.dequeue()

	try:
		Q = CircularQueue(0)
	except Exception as e:
		print e
