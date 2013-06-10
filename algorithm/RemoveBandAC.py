def removeBandAC(A):
	print A, '->',
	A = list(A)
	i = 0
	while i < len(A):
		deleted = False
		if A[i] == 'b':
			del A[i]
			deleted = True
		elif A[i] == 'a':
			if (i+1) < len(A) and A[i+1] == 'c':
				del A[i]
				del A[i]
				deleted = True
		if not deleted:
			i += 1
	for i in xrange(0, len(A)):
		if A[i] is not None:
			print A[i],
	print

if __name__ == '__main__':
	A = 'b'
	removeBandAC(A)
	A = 'bbbbbbabcb'
	removeBandAC(A)
	A = 'bac'
	removeBandAC(A)
	A = 'bca'
	removeBandAC(A)
	A = 'acacacaca'
	removeBandAC(A)
	A = ''
	removeBandAC(A)
