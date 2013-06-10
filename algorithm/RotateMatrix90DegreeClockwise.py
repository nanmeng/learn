def rotateMatrix90DegreeClockwise(M, n):
	# square matrix (n*n)
	# (r, c) => (c, (n-1)-r)
	for r in xrange(0, n):
		for c in xrange(r, n-r-1):
			# print '(', r, c, ')'
			# 2 print '(', c, n-1-r, ')'
			# 3 print '(', n-1-r, n-1-c, ')'
			# 4 print '(', n-1-c, r, ')'

			# print '-------'
			temp = M[r][c]
			# printM(M, n)
			M[r][c] = M[n-1-c][r]
			# printM(M, n)
			M[n-1-c][r] = M[n-1-r][n-1-c]
			# printM(M, n)
			M[n-1-r][n-1-c] = M[c][n-1-r]
			# printM(M, n)
			M[c][n-1-r] = temp
			# printM(M, n)
	return M

def printM(M, n):
	for r in xrange(0, n):
		for c in xrange(0, n):
			print M[r][c],
		print
	print

if __name__ == '__main__':
	M = [
			['2','2','2','2','2','2','2','2','2'],
			['3','x','x','x','1','x','x','x','1'],
			['3','z','n','n','3','n','n','q','1'],
			['3','z','s','A','4','R','t','q','1'],
			['3','4','2','3','e','1','4','2','1'],
			['3','z','s','B','2','E','t','q','1'],
			['3','z','m','m','1','m','m','q','1'],
			['3','y','y','y','3','y','y','y','1'],
			['4','4','4','4','4','4','4','4','4'],
			]
	printM(M, 9)
	M = rotateMatrix90DegreeClockwise(M, 9)
	printM(M, 9)
