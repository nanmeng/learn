class P(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def toString(self):
		return '(' + self.x + ',' + self.y +')'

def getLineKandB(p1, p2):
	# given two points p1 and p2 which will form a line
	# (if p1 and p2 are not identical)
	# this should return the K and B for the line
	# in the line formula y = Kx + B

	if p1.x == p2.x and p1.y == p2.y:
		return None
	K = float((p1.y - p2.y) / (p1.x - p2.x))
	B = p1.y - (K * p1.x)
	return [K, B]

def findLineContainingMostPoints(P):
	# given a point list

# TODO this is not finished, obviously
