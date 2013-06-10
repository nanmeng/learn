def longestIncreasingSubsequence(A):
	# CONSECUTIVE VERSION
	# keep two indices
	# one for the start of the increasing subseq
	# one for the end of the increasing subseq

	# try extending the end and see if the subseq is still increasing
	# if it is, then keep extending the end index
	# if it is no longer an increasing subseq
	# move the start index to where the end index is to begin new probe

	# while doing all these, keep track of the longest increasing subseq found
	s = 0
	e = 0
	longest_s = 0
	longest_e = 0
	longest = 0
	while e < len(A):
		print 'A[',e,']',A[e],':','A[',s,']',A[s]
		print longest_s, longest_e
		if e > s:
			if A[e] > A[e-1]:
				# if we are still seeing an increasing subseq
				if ((e-s)+1) > longest:
					# remember it if this subseq is longest
					longest_s = s
					longest_e = e
					longest = e-s+1
				# try extending the end to try a longer subseq
				e += 1
			else:
				# if the subseq is not increasing any more
				# bring the start index to where the end is
				# to start a new probe again
				s = e
				e += 1
		elif e == s:
			# s and e are at the same spot, only one item
			# we consider it as an increasing subseq
			if ((e-s)+1) > longest:
				longest_s = s
				longest_e = e
				longest = e-s+1
			e += 1
		else:
			raise Exception('e < s: how did this happen?')
	return [longest, longest_s, longest_e]

if __name__ == '__main__':
	A = [1,2,3,4,-1,2,5,6,9,12,2,3,1,1,3]
	print longestIncreasingSubsequence(A)
