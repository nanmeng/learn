def removeDuplicatesFromSortedArray(A):
	if len(A) <= 0:
		return A
	i = 0
	j = i+1
	last_seen = A[i]
	while j < len(A):
		if A[j] != last_seen:
			last_seen = A[j]
			i += 1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
		j += 1
	for n in xrange(j-1, i, -1):
		del A[n]
	return A

if __name__ == '__main__':
	A = [1,1,2,3,4,5,6,6,6,6,6,6,7,7]
	print removeDuplicatesFromSortedArray(A)
	A = [1,1,1,1,1,1,1,1,1,1,1,1,1]
	print removeDuplicatesFromSortedArray(A)
	A = []
	print removeDuplicatesFromSortedArray(A)
	A = [1,1,1,1,1,1,1,1,1,1,1,1,1,6]
	print removeDuplicatesFromSortedArray(A)
	A = [1,2,3,4,5,6]
	print removeDuplicatesFromSortedArray(A)
	A = [2,4,100,100,100,2030]
	print removeDuplicatesFromSortedArray(A)
