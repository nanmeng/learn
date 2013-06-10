# TODO This script has problem!
def merge(LIST, L, R, M):
	left = LIST[L:M+1]
	left_len = len(left)
	right = LIST[M+1:R+1]
	right_len = len(right)
	left_idx = 0
	right_idx = 0
	for i in xrange(L, R):
		if left_idx == left_len:
			LIST[i] = right[right_idx]
			right_idx += 1
		elif right_idx == right_len:
			LIST[i] = left[left_idx]
			left_idx += 1
		else:
			if left[left_idx] <= right[right_idx]:
				LIST[i] = left[left_idx]
				left_idx += 1
			else:
				LIST[i] = right[right_idx]
				right_idx += 1

def mergeSort(LIST, L, R):
	if L < R:
		idx = (L + R) / 2
		print L
		print R
		print idx
		mergeSort(LIST, L, idx)
		mergeSort(LIST, idx+1, R)
		merge(LIST, L, R, idx)

if __name__ == '__main__':
	L = [2,3,45,67,7,8,5,5,6,7,88,4,4,272]
	mergeSort(L, 0, len(L)-1)
	print L
