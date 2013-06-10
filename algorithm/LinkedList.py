class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = self.head

	def append(self, node):
		if not self.tail:
			self.tail = node
			if not self.head:
				self.head = self.tail
		else:
			self.tail.next = node
			self.tail = self.tail.next

	def remove(self, value):
		if not self.head:
			print 'nothing to remove'
			return
		while self.head.value == value:
			self.head = self.head.next
			if not self.head:
				return
		cur_node = self.head
		while cur_node:
			if cur_node.next:
				if cur_node.next.value == value:
					cur_node.next = cur_node.next.next
				else:
					cur_node = cur_node.next
			else:
				return

	def toString(self):
		cur_node = self.head
		while cur_node:
			print cur_node.value,
			cur_node = cur_node.next
		print

if __name__ == '__main__':
	A = [1,1,2,3,5,5,33,5,2,2,2,1,3,3,5,2,43,43,33]
	L = LinkedList()
	for i in xrange(0, len(A)):
		L.toString()
		L.append(Node(A[i]))
	L.remove(5)
	L.toString()
	L.remove(1)
	L.toString()
	L.remove(43)
	L.toString()
	L.remove(3)
	L.toString()
	L.remove(33)
	L.toString()
	L.remove(2)
	L.toString()
