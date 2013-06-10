def printListPermutation(A, prefix=[]):
	# print '---- A', A
	# print '---- prefix', prefix
	if len(A) == 1:
		prefix.append(A[0])
		print "PRINT:", prefix
		prefix.pop()
		return
	for i in xrange(0, len(A)):
		C = A[0:]
		# print '--C1', C
		prefix.append(C[i])
		for j in xrange(i, 0, -1):
			C[j] = C[j-1]
		# print '--C2', C
		printListPermutation(C[1:], prefix)
		prefix.pop()

if __name__ == '__main__':
	A = [12,4,66,8,9]
	A.sort(reverse=True)
	print A
	printListPermutation(A)
