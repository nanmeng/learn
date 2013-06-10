def shortestSubsequenceWithAllWords(D, words):
	# give a large document and a list of words find the
	# shortest subsequence in the document that contains
	# all the words in the list.  order does not matter

	# the intuitive thought would be like this: since it
	# is a large document, plus we need to know where the
	# subsequence is, we do not consider sorting.  We use
	# different indices to traverse the document while
	# keeping track of the positions where words are found

	# for example, if there are 3 words given in the list
	# use probably 3 indices to track the position where
	# the 1st, 2nd, and 3rd word is found respectively.
	# initially, those indices are all -1 to indicate that
	# no such word is found yet.
	
	# everytime we found a word, update the latest found
	# index for that word.  this way the latest found index
	# will always tell us where the closest the index of
	# a given word is.  also we check if all words have
	# been found, and calculate the length of the subsequence
	# containing all words, and compare this length with
	# the shortest length we have seen up to that moment
	# if the current length is shorter, update the shortest
	# length record, which probably should contain the indices
	# correspond to the shortest length subsequence
	idx = {}
	expecting = []
	# init the idx hash for the words
	for w in words:
		idx[w] = -1
		expecting.append(w)
	# we expect to see the words
	num_words = len(words)
	num_words_seen = 0
	shortest_len = float('inf')
	shortest_s = -1
	shortest_e = -1
	for i in xrange(0, len(D)):
		# print 'word:', D[i]
		# print 'idx:', idx
		if idx.has_key(D[i]):
			if idx[D[i]] < 0:
				# if this word was not seen before
				num_words_seen += 1
			idx[D[i]] = i
			if num_words_seen == num_words:
				s = min(idx.values())
				e = max(idx.values())
				# print 's:', s, 'e:', e
				l = e-s+1
				if l < shortest_len:
					shortest_len = l
					shortest_s = s
					shortest_e = e
		i += 1
	return [shortest_s, shortest_e]

if __name__ == '__main__':
	words = ['W1', 'W2', 'W3', 'W4']
	D = list('W3 qwer qwe gq gqef qewfqerg W1 qejflqjlj W4 W1 a W2 W3 W1 W2 W2 asdfadf W3'.split(' '))
	print shortestSubsequenceWithAllWords(D, words)
