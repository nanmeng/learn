# first compare the lengths of the lists
# X should be at least longer than Y, else
# return None

# then, the idea is, first sort X to be non-decreasing

# for the input Y, check from its first digit

# we try to find a digit in X, which shall be at
# least equal the current digit in Y

# if found, we try to find the least greater X rearrangement
# for X and Y excluding the currently used digits

def rearrangeXToBeLeastGreaterThanY(X, Y):
	print '----', X, Y
	if len(X) < len(Y):
		return False

	if len(Y) == 1:
		if len(X) > 1 or X[0] > Y[0]:
			return X
		else:
			return False

	if len(Y) == 0:
		if len(X) > 0:
			return X

	# make a copy of X
	trial = X[0:]
	for i in xrange(0, len(Y)):
		print 'X:', X, 'Y:', Y
		print 'X[',i,']',X[i],'Y[0]',Y[0]
		if X[i] == Y[0]:
			# move X[i] to be the first digit of X
			digit = X[i]
			x = X[0:]
			for n in xrange(i, 0, -1):
				x[n] = x[n-1]
			x[0] = digit
			result = rearrangeXToBeLeastGreaterThanY(x[1:], Y[1:])
			if result is not False:
				print 'RESULT:',
				result = [digit] + result
				print result
				return result
		elif X[i] > Y[0] and len(X) >= len(Y):
			print 'RESULT:',
			digit = X[i]
			digit = X[i]
			x = X[0:]
			for n in xrange(i, 0, -1):
				x[n] = x[n-1]
			x[0] = digit
			print x

	return False


if __name__ == '__main__':
	X = [1,2,3,4]
	Y = [2,4,1,0]
	X.sort()
	print X
	print Y
	rearrangeXToBeLeastGreaterThanY(X, Y)
