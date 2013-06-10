def findMaxCrossingSubarray(A, low, mid, high):
	left = mid
	max_left = float('-inf')
	sum_left = 0
	max_left_idx = left
	while left >= low:
		sum_left += A[left]
		if sum_left > max_left:
			max_left = sum_left
			max_left_idx = left
		left -= 1
	right = mid + 1
	max_right = float('-inf')
	sum_right = 0
	max_rigth_idx = right
	while right <= high:
		sum_right += A[right]
		if sum_right > max_right:
			max_right = sum_right
			max_right_idx = right
		right += 1
	return [max_left_idx, max_right_idx, max_left + max_right]

def findMaxSubarray(A, low, high):
	if low >= high:
		return [low, high, A[low]]
	mid = (low + high) / 2
	max_left = findMaxSubarray(A, low, mid)
	max_right = findMaxSubarray(A, mid+1, high)
	max_cross = findMaxCrossingSubarray(A, low, mid, high)
	if max_left[2] > max_right[2] and max_left[2] > max_cross[2]:
		return max_left
	elif max_right[2] > max_left[2] and max_right[2] > max_cross[2]:
		return max_right
	else:
		return max_cross

if __name__ == '__main__':
	A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
	print findMaxSubarray(A, 0, len(A)-1)
