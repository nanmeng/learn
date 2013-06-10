def findIndicesIJK(A):
	# given list (array) A
	# find three indices i < j < k
	# so that A[i] < A[j] < A[k]

	# idea:
	# set i to 0
	# set k to last index
	# if A[i] > A[k]:
		# s_index = i
		# if A[i+1] < A[i]:
			# s_index = i+1
		# if A[s_index] 
		# greater index = k
		# if A[k-1] > A[k]:
			# greater index = k-1
	# compare A[i+1] and A[k]
	# compare A[i] and A[k-1]

	# TODO WRONG IDEA!

	M = {}
