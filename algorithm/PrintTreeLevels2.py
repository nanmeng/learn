class TreeNode(object):
	def __init__(self, v):
		self.v = v
		self.left = None
		self.right = None

def printTreeLevels(node, height=0, M={}):
	if not M.has_key(height):
		M[height] = []
	M[height].append(node.v)
	if node.left:
		printTreeLevels(node.left, height+1, M)
	if node.right:
		printTreeLevels(node.right, height+1, M)
	return M

if __name__ == '__main__':
	n1 = TreeNode(1)
	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n4 = TreeNode(4)
	n5 = TreeNode(5)
	n6 = TreeNode(6)
	n7 = TreeNode(7)
	n8 = TreeNode(8)
	n1.left = n2
	n1.right = n3
	n2.left = n4
	n2.right = n5
	n3.left = n6
	n3.right = n7
	n4.left = n8
	M = printTreeLevels(n1)
	print M
