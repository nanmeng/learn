def hasTwoThatSum(LIST, SUM):
	LIST = quickSort(LIST)
	left = 0
	right = len(LIST)-1
	while left != right:
		s = LIST[left] + LIST[right]
		if s > SUM:
			right -= 1
		elif s < SUM:
			left += 1
		else:
			print 'yes:', LIST[left], '+', LIST[right], '=', SUM
			return

def quickSort(LIST):
	if len(LIST) <= 1:
		return LIST
	pivot = LIST[(len(LIST) - 1) / 2]
	LIST.remove(pivot)
	smaller = []
	greater = []
	for i in xrange(0, len(LIST)):
		if LIST[i] <= pivot:
			smaller.append(LIST[i])
		else:
			greater.append(LIST[i])
	return quickSort(smaller) + [pivot] + quickSort(greater)

if __name__ == '__main__':
	L = [2,5,5,61,1,4,6,7,10,12,9,8,2,454,10]
	print quickSort(L)
	hasTwoThatSum(L, 11)
	hasTwoThatSum(L, 10)
	hasTwoThatSum(L, 65)
	hasTwoThatSum(L, 1000)
	hasTwoThatSum(L, 459)
