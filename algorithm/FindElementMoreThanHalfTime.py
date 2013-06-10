def findElementMoreThanHalfTime(A):
	length = 0
	i = 0
	counts = {}
	while True:
		try:
			a = A[i]
		except IndexError:
			break
		print length,
		length += 1
		print counts
		counts[a] = counts.get(a, 0) + 1
		i += 1
	for k in counts:
		if counts[k] > (length / 2):
			print k
			return
	print -1

if __name__ == '__main__':
	A = [1,2,3,4,5,6,3,2,12,6,3,2,2,2,2,2,2,2]
	findElementMoreThanHalfTime(A)
