class TreeNode(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None

def printTreeLevels(N, height=0, A={}):
	# given a tree node, print every level in the
	# tree that has this node as the root. Each
	# level is printed on its own line

	# height is the height of the tree node N

	# A is the dict of list of nodes grouped by their height

	# the idea is that we do any traversal on the
	# tree while keeping track of the height of
	# the current tree node, and append that tree
	# node to the corresponding list indexed by
	# the height of the nodes in the list
	if not N:
		return
	if not A.has_key(height):
		A[height] = []
	A[height].append(N.value)
	printTreeLevels(N.left, height+1, A)
	printTreeLevels(N.right, height+1, A)

if __name__ == '__main__':
	n = []
	for i in xrange(0, 10):
		n.append(TreeNode(i))
	x = 0
	while x < len(n):
		if (x*2+1) < len(n):
			n[x].left = n[x*2+1]
		if ((x+1)*2) < len(n):
			n[x].right = n[(x+1)*2]
		x += 1
	A = {}
	printTreeLevels(n[0], 0, A)
	print A
