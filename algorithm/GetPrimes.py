def getPrimes(N):
	# get all primes less than or equal to N
	if N <= 1:
		return []
	P = []
	for i in xrange(0, N+1):
		P.append(None)
	P[0] = False
	P[1] = False
	n = 2
	while n <= N:
		# print P
		# print 'n =', n
		if n % 2 == 0 and n != 2:
			P[n] = False
			n += 1
			continue
		if P[n] is None:
			P[n] = True
			print 'P[', n, '] =', P[n]
			t = 2
			while (t * n) <= N:
				P[t * n] = False
				t += 1
		n += 1
	print
	return P

if __name__ == '__main__':
	getPrimes(100)
