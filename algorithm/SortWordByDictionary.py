def partition(A, lo, hi, D):
	if lo >= hi:
		return
	key = A[hi]
	i = lo - 1
	j = lo
	while j < hi:
		if D[A[j]] < D[key]:
			i += 1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
		j += 1
	temp = A[i+1]
	A[i+1] = A[hi]
	A[hi] = temp
	return i+1

def quickSort(A, lo, hi, D):
	if lo < hi:
		pivot = partition(A, lo, hi, D)
		quickSort(A, lo, pivot-1, D)
		quickSort(A, pivot+1, hi, D)

if __name__ == '__main__':
	A = list('SHEEP')
	X = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	D = {}
	i = 0
	while i < len(X):
		D[X[i]] = i
		i += 1
	print D
	quickSort(A, 0, len(A)-1, D)
	print A

	X2 = list('ZYXWVUTSRQPONMLKJIHGFEDCBA')
	D2 = {}
	i = 0
	while i < len(X2):
		D2[X2[i]] = i
		i +=1
	print D2
	quickSort(A, 0, len(A)-1, D2)
	print A
