def findCommonElementsInSortedSets(A, B):
	# initialize two indices i and j, for A and B respectively
	i = 0
	j = 0
	# keep track of the common elements
	common = []
	# traverse the two sorted sets (arrays) using the indices
	# if we exhaust one of the sets, we stop the traversal
	while i < len(A) and j < len(B):
		if A[i] == B[j]:
			# if the two items match
			# keep the record
			common.append(A[i])
			# compare the next pair
			i += 1
			j += 1
		elif A[i] > B[j]:
			# if the item in A is larger
			# try the next larger item in B since it may match
			j += 1
		else:
			# if the item in B is larger
			# try the next larger item in A since it may match
			i += 1
	last_seen = None
	for x in common:
		if not (last_seen == x):
			print x

if __name__ == '__main__':
	A = [1,2,3,4,5,5,5,5,6,6,9]
	B = [5,6,7,8,9,9]
	findCommonElementsInSortedSets(A, B)
