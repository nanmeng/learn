def allInterleavingsOfTwoStrings(A, B, prefix=[]):
	# select 0 to len(A) chars from A
	# select 0 to len(B) chars from B
	# then print allInterleavingsOfTwoStrings
	# for the rests of A and B
	'''
	print
	print 'P:', prefix
	print 'A:', A
	print 'B:', B
	'''
	if len(A) == 0:
		print ''.join(prefix) + ''.join(B)
		return
	if len(B) == 0:
		print ''.join(prefix) + ''.join(A)
		return

	# print all interleavings w/ A[0] as prefix
	prefix.append(A[0])
	Ap = A[1:]
	allInterleavingsOfTwoStrings(Ap, B, prefix)
	prefix.pop()

	# print all interleavings w/ B[0] as prefix
	prefix.append(B[0])
	Bp = B[1:]
	allInterleavingsOfTwoStrings(A, Bp, prefix)
	prefix.pop()

if __name__ == '__main__':
	A = list('ABCZ')
	B = list('DE')
	allInterleavingsOfTwoStrings(A, B)
