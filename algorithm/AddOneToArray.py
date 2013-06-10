def addOneToArray(A):
	power = 1
	upgrade = 1
	for i in xrange(len(A)-1, -1, -1):
		s = A[i] + upgrade
		digit = s % 10
		upgrade = s / 10
		A[i] = digit
	if upgrade > 0:
		A = [upgrade] + A
	return A

if __name__ == '__main__':
	A = [7,3,5,3,9]
	print addOneToArray(A)
	A = [9,9,9,9,9,9,9,9]
	print addOneToArray(A)
	A = [9]
	print addOneToArray(A)
	A = [0]
	print addOneToArray(A)
