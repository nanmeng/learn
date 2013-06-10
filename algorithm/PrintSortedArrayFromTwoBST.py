class TN(object):
	# TreeNode class
	def __init__(self, i, value):
		# id
		self.i = i
		self.v = value
		self.left = None
		self.right = None
		# parent
		self.p = None
	def toString(self):
		s = '(' + str(self.i) + ': ' + str(self.v) + ' left:'
		if self.left is not None:
			s += str(self.left.i)
		else:
			s += 'x'
		s += ' right:'
		if self.right is not None:
			s += str(self.right.i)
		else:
			s += 'x'
		s += ')'
		return s

def minSubtree(node):
	# return the min value in subtree rooted at node
	if node is None:
		return None
	while node.left is not None:
		node = node.left
	return node

def successor(node):
	# print '--- successor', node.toString()
	# return the successor of BST node
	if node.p is None:
		# root
		if node.right:
			return minSubtree(node.right)
		else:
			return None
	if node.right:
		# has right subtree
		return minSubtree(node.right)
	# node has no right child from here down
	if node == node.p.left:
		# node is a left child
		return node.p
	if node == node.p.right:
		# node is a right child
		np = node.p
		pp = np.p
		while pp and np != pp.left:
			np = pp
			pp = np.p
		return pp

def printRestOfTree(node):
	# print the tree from node following successor path
	while node is not None:
		print node.v,
		node = successor(node)

def printSortedArrayFromTwoBST(T1, T2):
	# T1 and T2 shall be the roots of those two trees

	# start from the minimums of the two trees
	min1 = minSubtree(T1)
	min2 = minSubtree(T2)
	while True: 
		'''
		print 'min1:',
		if min1:
			print min1.toString()
		else:
			print min1
		print 'min2:',
		if min2:
			print min2.toString()
		else:
			print min2
		'''
		if min1 is None:
			printRestOfTree(min2)
			return
		if min2 is None:
			printRestOfTree(min1)
			return
		if min1.v <= min2.v:
			print min1.v
			min1 = successor(min1)
		else:
			print min2.v
			min2 = successor(min2)

if __name__ == '__main__':
	n0 = TN(0, 3)
	n1 = TN(1, 1)
	n2 = TN(2, 5)
	n3 = TN(3, 4)
	n4 = TN(4, 2)
	n5 = TN(5, 6)
	n0.left = n1
	n1.p = n0
	n0.right = n2
	n2.p = n0
	n3.left = n4
	n4.p = n3
	n3.right = n5
	n5.p = n3
	print '-----'
	print n0.toString()
	print n1.toString()
	print n2.toString()
	print n3.toString()
	print n4.toString()
	print n5.toString()
	print '-----'
	printSortedArrayFromTwoBST(n0, n3)
