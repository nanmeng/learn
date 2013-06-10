class Node(object):
	def __init__(self, value):
		self.prev = None
		self.next = None
		self.value = value

class DoubleLinkedList(object):
	def __init__(self):
		self.head = Node(None)
		self.tail = self.head

	def append(self, value):
		if self.head.value is None:
			self.head.value = value
			newtail = Node(None)
			self.tail = newtail
			self.tail.prev = self.head
			self.head.next = self.tail
		else:
			self.tail.value = value
			newtail = Node(None)
			newtail.prev = self.tail
			self.tail.next = newtail
			self.tail = newtail

	def toString(self):
		i = self.head
		while i.value:
			print i.value,
			i = i.next
		print

def addTwoDoubleLinkedListNumbers(A, B):
	a = A.tail.prev
	b = B.tail.prev
	if a is None:
		return 0
	upgrade = 0
	total = 0
	power = 1
	while a is not None:
		print a.value, b.value
		s = a.value + b.value
		remain = s % 10
		total += ((remain + upgrade) * power)
		upgrade = s / 10
		power = power * 10
		a = a.prev
		b = b.prev
	if upgrade > 0:
		total += (upgrade * power)
	return total

if __name__ == '__main__':
	A = DoubleLinkedList()
	A.append(1)
	A.append(2)
	A.append(3)
	A.toString()
	B = DoubleLinkedList()
	B.append(9)
	B.append(8)
	B.append(7)
	A.toString()

	print addTwoDoubleLinkedListNumbers(A, B)
