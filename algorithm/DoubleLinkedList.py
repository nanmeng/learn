def remove(head, value):
	cur = head
	while cur != None:
		if cur.value == value:
			if cur.prev != None:
				cur.prev.next = cur.next
			if cur.next != None:
				cur.next.prev = cur.prev
			break
		cur = cur.next

class Node(object):
	def __init__(self):
		self.prev = None
		self.next = None
		self.value = None

class DoubleLinkedList(object):
	def __init__(self):
		self.head = Node()
		self.tail = self.head

	def append(self, value):
		self.tail.value = value
		newtail = Node()
		self.tail.next = newtail
		newtail.prev = self.tail
		self.tail = newtail

	def toString(self):
		i = self.head
		while i.value:
			print i.value
			i = i.next

def myRemove(head, value):
	node = head
	while node:
		if node.value == value:
			if node.prev:
				node.prev.next = node.next
			if node.next:
				node.next.prev = node.prev
		node = node.next

if __name__ == '__main__':
	L = DoubleLinkedList()

	L.append(1)
	L.append(2)
	L.append(3)
	L.append(4)

	print L.toString()

	remove(L.head, 3)
	print L.toString()

	L.append(5)
	L.append(6)
	L.append(6)
	L.append(6)
	L.append(6)
	L.append(6)
	L.append(7)
	L.append(7)
	L.append(7)
	L.append(7)
	L.append(7)
	print L.toString()

	myRemove(L.head, 6)
	print L.toString()

	remove(L.head, 5)
	print L.toString()

