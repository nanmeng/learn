class R(object):
	# Rectangles
	def __init__(self, i, ul, br):
		self.i = i
		self.ul = ul
		self.br = br
		self.b = br.y
		self.r = br.x
		self.l = ul.x
		self.t = ul.y
	def toString(self):
		return self.i,self.ul.toString() + ' - ' + self.br.toString()

class C(object):
	# Coordinates
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def toString(self):
		return '(' + str(self.x) + ',' + str(self.y) + ')'

def overlap(R1, R2):
	# print '?', R1.toString(), R2.toString()
	# check if the two rectangles overlap
	if not(R1.b >= R2.t or R1.t <= R2.b) and not(R1.l >= R2.r or R1.r <= R2.l):
		return True
	else:
		return False

def overlapRectangles(listR):
	# find all pairs of overlapping rectangles
	# from the list of given axis-aligned rectangles

	# the first idea is about going over all
	# the rectangles and see if the current one
	# overlaps with any of the rest.  if there is
	# overlap then we print the pair.  we only
	# check the current rectangle with the ones
	# that come after it in the list, because the
	# ones that come before it has been checked in
	# previous iterations
	for i in xrange(0, len(listR)):
		j = i + 1
		R1 = listR[i]
		while j < len(listR):
			R2 = listR[j]
			if overlap(R1, R2):
				print R1.toString(),'overlap',R2.toString()
			j += 1

if __name__ == '__main__':
	C1  = C(-2, 5)
	C2  = C( 2, 4)
	C3  = C(-3, 3)
	C4  = C( 3, 3)
	C5  = C(-4, 2)
	C6  = C(-1, 2)
	C7  = C( 1, 1)
	C8  = C( 4, 1)
	C9  = C(-3,-1)
	C10 = C( 1,-1)
	C11 = C(-2,-2)
	C12 = C( 2,-2)
	C13 = C( 5,-2)
	C14 = C( 3,-3)
	C15 = C( 2,-4)
	R1 = R(1, C1, C4)
	R2 = R(2, C3, C7)
	R3 = R(3, C2, C6)
	R4 = R(4, C5,C11)
	R5 = R(5, C6,C15)
	R6 = R(6, C2,C13)
	R7 = R(7, C9,C14)
	R8 = R(8,C10,C12)
	listR = [R1,R2,R3,R4,R5,R6,R7,R8]
	overlapRectangles(listR)
