def LEFT(i):
	return 2 * i + 1

def RIGHT(i):
	return LEFT(i) + 1

def PARENT(i):
	return i / 2

def maxHeapify(A, i, size):
	print 'parent:', i, A[i]
	left = LEFT(i)
	right = RIGHT(i)
	if left < size:
		print 'left:  ', left, A[left]
	if right < size:
		print 'right: ', right, A[right]
	largest = i
	if left < size and A[left] > A[i]:
		largest = left
	else:
		largest = i
	if right < size and A[right] > A[largest]:
		largest = right
	if largest != i:
		print 'Switch', A[largest], 'with', A[i]
		temp = A[i]
		A[i] = A[largest]
		A[largest] = temp
		print A
		maxHeapify(A, largest, size)

def buildMaxHeap(A):
	for i in xrange(len(A)/2, -1, -1):
		maxHeapify(A, i, len(A))

def heapSort(A):
	buildMaxHeap(A)
	size = len(A)
	print "SORT BEGIN"
	for i in xrange(len(A)-1, 0, -1):
		print A
		print 'Switch', A[i], 'with', A[0]
		temp = A[i]
		A[i] = A[0]
		A[0] = temp
		size -= 1
		maxHeapify(A, 0, size)

if __name__ == '__main__':
	A = [4,1,3,2,16,9,10,14,8,7]
	print A
	heapSort(A)
	print A
