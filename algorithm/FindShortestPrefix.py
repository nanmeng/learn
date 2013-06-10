def findShortestPrefix(W, L):
	# return the shortest prefix of word W
	# that is not the prefix of any word in the list L

	# ignore the empty string case, cuz it is
	# a prefix of everything

	# start from the first char in W
	# if any word in L has the same first char
	# then first char is not the shortest prefix
	# we are looking for; otherwise, it is
	prefix = ''
	i = 0
	while len(L) > 0 and i < len(W):
		increased = False
		n = 0
		while n < len(L):
			if L[n][i] != W[i]:
				print 'remove:', L[n]
				del L[n]
			else:
				if not increased:
					prefix += W[i]
					increased = True
			n += 1
		i += 1
	return prefix

if __name__ == '__main__':
	W = list('cat')
	L = ['alpha', 'beta', 'cotton', 'delta', 'camera']
	for i in xrange(0, len(L)):
		L[i] = list(L[i])
	print findShortestPrefix(W, L)
