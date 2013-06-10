def findNumberInSquareMatrix(v, M):
	# find number v in square matrix M (n x n)
	n = len(M)
	if v < M[0][0] or v > M[n-1][n-1]:
		return None
	row = -1
	while (row+1) < n:
		print 'row:', row+1
		if M[row+1][n-1] < v:
			print row+1, n-1, M[row+1][n-1]
			row += 1
			continue
		print row+1, n-1, M[row+1][n-1]
		if M[row+1][n-1] == v:
			return [row+1, n-1]
		else:
			for i in xrange(1, n):
				print row+1, i, M[row+1][i]
				if M[row+1][i] == v:
					return [row+1, i]
			row += 1
	col = -1
	while (col+1) < n:
		print 'col:', col+1
		if M[n-1][col+1] < v:
			print n-1, col+1, M[n-1][col+1]
			col += 1
			continue
		print n-1, col+1, M[n-1][col+1]
		if M[n-1][col+1] == v:
			return [n-1, col+1]
		else:
			for i in xrange(1, n):
				print i, col+1, M[i][col+1]
				if M[i][col+1] == v:
					return [i, col+1]
			col +=1
	return None

if __name__ == '__main__':
	M = [
			[0,1,2,4],
			[2,3,5,6],
			[4,5,6,10],
			[6,8,9,11]
			]
	print findNumberInSquareMatrix(7, M)
