def C(n):
	if n <= 0:
		return 0
	if n == 1:
		return 1
	total = 0
	for i in xrange(1,4):
		if n-i == 0:
			total += 1
			continue
		ways = C(n-i)
		if ways > 0:
			total = total + ways
	return total

if __name__ == '__main__':
	print C(1)
	print C(2)
	print C(3)
	print C(4)
	print C(5)
	print C(6)
