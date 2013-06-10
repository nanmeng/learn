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

def findLongestSpelledInDictionary(D, letters):
	# given a dictionary D, and an array of letters
	# find the longest word in the dict that can be
	# spelled with the collection of letters
	# here the D can actually just be an array of words
	sL = list(letters)
	# sL = quickSort(letters)
	quickSort(sL, 0, len(sL)-1)
	print sL
	matched_map = {}
	for word in D:
		sW = list(word)
		quickSort(sW, 0, len(sW)-1)
		print sL
		print sW
		i = 0
		j = 0
		matched = 0
		while j < len(sW):
			print 'trying:', sW[j], '-', sL[i],
			# try to find current letter in sorted word
			# in the sorted letters, from the smallest
			# letter to the largest letter
			if sW[j] == sL[i]:
				# if the two letter are the same
				# we matched one pair
				matched += 1
				# continue to compare the next pair
				i += 1
				j += 1
				print 'next pair'
			elif sW[j] > sL[i]:
				# else if current letter in sorted word
				# is larger than the current letter in sorted letters
				# try the next letter in sorted letters
				i += 1
				print 'next letter'
			elif sW[j] < sL[i]:
				# else if current letter in sorted word
				# is smaller than the current letter in sorted letters
				# we will not be able to find this letter in sorted
				# word from the sorted letters any more
				# write down the number of letters matched for this word
				print 'break'
				# continue with the next word
				break
		if not (matched in matched_map):
			matched_map[matched] = []
		matched_map[matched].append(word)
		print 'matched_map:', matched_map

	max_matched = -1
	for k in matched_map:
		if k > max_matched:
			max_matched = k
	return [ max_matched, matched_map[max_matched] ]

if __name__ == '__main__':
	D = ['abacus','deltoid','gaff','giraffe','microphone','reef','qar']
	letters = ['a','e','f','f','g','i','r','q']
	print findLongestSpelledInDictionary(D, letters)
