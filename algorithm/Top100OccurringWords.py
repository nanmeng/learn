class Node(object):
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None
	def toString(self):
		return '(' + str(self.value) + ')'

class DoubleLinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0
		self.tail = self.head
	def add(self, node):
		if self.tail is None:
			self.tail = node
			self.head = node
		else:
			node.prev = self.tail
			self.tail.next = node
			self.tail = self.tail.next
		self.size += 1
	def place(self, node, word_count=None):
		if word_count is not None:
			print 'USING word_count',
		print 'PLACE:', node.toString()
		# add the given node in the right place
		# so that this list is sorted with head
		# to be the greatest
		if self.tail is None:
			self.add(node)
		else:
			n = self.tail
			print 'TAIL:', n.toString()
			while n:
				if word_count:
					print n.value, word_count[n.value], '<>', node.value, word_count[node.value]
					if word_count[n.value] < word_count[node.value]:
						n = n.prev
					else:
						break
				else:
					if n.value < node.value:
						n = n.prev
					else:
						break
			print '-', n.toString()
			if n is None:
				node.next = self.head
				self.head.prev = node
				self.head = node
				self.tail = self.head
				self.size += 1
			else:
				if word_count:
					if word_count[n.value] == word_count[node.value]:
						return
				else:
					if n.value == node.value:
						# no duplicates in list
						return
				if n.next:
					n.next.prev = node
				node.next = n.next
				node.prev = n
				n.next = node
				if n == self.tail:
					self.tail = node
				self.size += 1
		print 'PLACED:',
		print self.toString()
		print '- TAIL:',
		print self.tail.toString()
	def shrink(self):
		if self.tail is None:
			return
		else:
			self.tail = self.tail.prev
			self.tail.next = None
		self.size -= 1
	def remove(self, value):
		node = self.head
		while node:
			if node.value == value:
				if node.prev is None:
					node.next.prev = None
					self.head = node.next
				else:
					node.prev.next = node.next
					node.next.prev = node.prev
				self.size -= 1
			node = node.next
	def toString(self):
		node = self.head
		ret = '['
		while node:
			ret += node.toString()
			node = node.next
		ret += ']'
		return ret

def topOccurringWords(Docs, top):
	# given a set of documents, find the top (top) occurring words
	# e.g. top = 100, find the top 100 occurring words

	# the idea is that we traverse all the documents and keep track
	# of the top 100 occurring words. then output them at the end

	# we keep a word-to-occurrence dict (hash)

	# we also keep track of the 100th most occurring word
	# if there are not enough occurring words to fill up to the 100th
	# position, we just use the least occurring word in the top list
	# something like: least_occurrence_in_top

	# we keep a double linked list of the words in the top list
	# the tail being the least occurred word, this double linked list
	# size shall never exceed 100
	# something like: words_in_top

	# for each word seen, increase its occurrence count
	#
	# 1. if the size of words_in_top < 100
	#
	#    + (increase the size of the top list: list_size += 1)
	#
	#    + place the current word at the right position in the words_in_top list
	#
	# 2. if the number of top occurring words in the top list >= 100
	#
	#    + compare the count of the word at the tail of words_in_top
	#      with the occurrence of the current word
	#
	#        1. if the current word has more occurrence, place the
	#           current word into the words_in_top list, and remove
	#           the last item in the list
	#
	# at the end words_in_top will contain the top 100 occurring words

	# this should be a double linked list of double linked lists
	# each sub list has all the words with the same number of occurrences
	words_in_top = DoubleLinkedList()
	# a double linked list of top occurrence numbers
	occur_in_top = DoubleLinkedList()
	# map the occurrence to list of words having that occurrence
	word_lists = {}
	# map word to its occurrence
	word_count = {}
	for D in Docs:
		# for each doc
		for w in D:
			print w
			print word_count
			# print occur_in_top.toString()
			print words_in_top.toString()
			# for each word
			# get its number of occurrences
			wc = word_count.get(w, 0) + 1
			word_count[w] = wc

			# we can ignore this operation here:
			# remove this word from word_lists[wc-1]
			# and add this word to word_lists[wc]

			list_size = words_in_top.size
			if list_size < top:
				# node = Node(wc)
				# occur_in_top.place(node)
				wnode = Node(w)
				words_in_top.place(wnode, word_count)
				# place wc into list at the right position
			else:
				if wc > word_count[words_in_top.tail.value]:
					print 'wc > word_count[words_in_top.tail.value]'
					# node = Node(wc)
					# occur_in_top.place(node)
					wnode = Node(w)
					words_in_top.place(wnode, word_count)
					if words_in_top.size > top:
						words_in_top.shrink()
					# place wc into list at the right position
					# remove the tail from the list
	print words_in_top.toString()
	print word_count

if __name__ == '__main__':
	Docs = [
			list('w1 w1 w1 w1 w1 w1'.split(' ')),
			list('w1 w1 w1 w1 w1 w1'.split(' ')),
			list('w1 w1 w1 w1 w1 w1'.split(' ')),
			list('w1 w1 w1 w1 w1 w1'.split(' ')),
			list('w1 w1 w1 w1 w1 w1'.split(' ')),
			list('w1 w1 w1 w1 w1 w1'.split(' ')),
			list('w2 w2 w2 w2 w2 w2'.split(' ')),
			list('w2 w2 w2 w2 w2 w2'.split(' ')),
			list('w2 w2 w2 w2 w2 w2'.split(' ')),
			list('w2 w2 w2 w2 w2 w2'.split(' ')),
			list('w3 w3 w3 w3 w3 w3'.split(' ')),
			list('w3 w3 w3 w3 w3 w3'.split(' ')),
			list('w3 w3 w3 w3 w3 w3'.split(' ')),
			list('w4 w4 w4 w4 w4 w4'.split(' ')),
			list('w4 w4 w4 w4 w4 w4'.split(' ')),
			list('w5 w5 w5 w5 w5 w5'.split(' ')),
			];
	topOccurringWords(Docs, 3)
	topOccurringWords(Docs, 4)
