def findMaxSubarray(A, lo, hi):
	# use divide and conquer
	# divide the array into two parts
	# the max subarray may be in lo part
	# or the max subarray may be in hi part
	# or the max subarray may cross the mid point

	# if there is only one item in array
	# max subarray is from lo to hi
	# sum is A[lo]
	if lo == hi:
		return [A[lo], lo, hi]

	# do the divide first
	mid = (lo + hi) / 2
	# get the results from the two parts
	[maxLo, lo_L, lo_R] = findMaxSubarray(A, lo, mid)
	[maxHi, hi_L, hi_R] = findMaxSubarray(A, mid+1, hi)

	# try to find max subarray that crosses the middle
	i = mid
	j = mid+1
	# get the index where left part gets max total
	maxi = i
	maxj = j
	sumL = 0
	maxL = float('-inf')
	while i >= lo:
		sumL += A[i]
		if sumL > maxL:
			maxi = i
			maxL = sumL
		i -= 1
	sumR = 0
	maxR = float('-inf')
	while j <= (hi-1):
		sumR += A[j]
		if sumR > maxR:
			maxj = j
			maxR = sumR
		j += 1
	maxCross = maxL + maxR
	if maxLo > maxHi and maxLo > maxCross:
		return [maxLo, lo_L, lo_R]
	elif maxHi > maxLo and maxHi > maxCross:
		return [maxHi, hi_L, hi_R]
	else:
		return [maxCross, maxi, maxj]

if __name__ == '__main__':
	A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
	print findMaxSubarray(A, 0, len(A)-1)
