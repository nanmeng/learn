def mostOccurrenceInBST(node, o={}, maxo=0, maxy=[]):
	if node is None:
		return []
	# visit the left subtree
	# visit the right subtree
	# visit the current node
	if node.left:
		[o, maxo, maxy] = mostOccurrenceInBST(node.left, o)
	if node.right:
		[o, maxo, maxy] = mostOccurrenceInBST(node.right, o)
	o[node.value] = o.get(node.value, 0) + 1
	for key in o:
		if o[key] > maxo:
			maxo = o[key]
			maxy = []
			maxy.append(key)
		elif o[key] == maxo and key not in maxy:
			maxy.append(key)
	return [o, maxo, maxy]

class TreeNode(object):
	def __init__(self, i, value):
		self.i = i
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.level = None
	def toString(self):
		print 'i:', self.i,
		print 'level:', self.level,
		print 'value:', self.value,
		if self.parent:
			print 'parent:', self.parent.i,
		else:
			print 'parent:', self.parent,
		if self.left:
			print 'left:', self.left.i,
		if self.right:
			print 'right:', self.right.i,
		print

def addBSTNode(tnode, node, level):
	if tnode is None:
		node.level = level
		print 'added', node.toString()
		tnode = node
	else:
		if node.value <= tnode.value:
			if tnode.left is None:
				node.level = level+1
				tnode.left = node
				node.parent = tnode
				print 'added as left', node.toString()
			else:
				addBSTNode(tnode.left, node, level+1)
		else:
			# node.value >= tnode.value:
			if tnode.right is None:
				node.level = level+1
				tnode.right = node
				node.parent = tnode
				print 'added as right', node.toString()
			else:
				addBSTNode(tnode.right, node, level+1)

def BreadthFirstPrint(node, result={}):
	node.toString()
	print result
	if node is None:
		return result
	else:
		if node.left:
			result = BreadthFirstPrint(node.left, result)
		if not (node.level in result):
			result[node.level] = []
		result[node.level].append(node)
		if node.right:
			result = BreadthFirstPrint(node.right, result)
		return result

class BST(object):
	def __init__(self):
		self.root = None

	def addNode(self, node):
		if self.root is None:
			# node.toString()
			node.level = 0
			self.root = node
		else:
			addBSTNode(self.root, node, 0)

	def toString(self):
		result = BreadthFirstPrint(self.root)
		for key in result:
			print key
			for x in result[key]:
				x.toString()

if __name__ == '__main__':
	T = BST()
	A = [1,1,1,1,1,2,3,4,5,6,7,7,5,3,2,4,5,5,6,1,2,3,4,4,6,6,8,4,2,5,7,8]
	for i in xrange(0, len(A)):
		T.addNode(TreeNode(i, A[i]))
	T.toString()
	print mostOccurrenceInBST(T.root)
