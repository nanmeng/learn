def quickSort(A, low, high):
	if low < high:
		mid = partition(A, low, high)
		quickSort(A, low, mid-1)
		quickSort(A, mid+1, high)

def partition(A, low, high):
	x = A[high]
	i = low - 1
	for j in xrange(low, high):
		if A[j] <= x:
			i += 1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
	temp = A[i+1]
	A[i+1] = A[high]
	A[high] = temp
	return i+1

if __name__ == '__main__':
	A = [3,5,67,7,5,5,7,72,234,7,8,2,34,55]
	print A
	quickSort(A, 0, len(A)-1)
	print A
