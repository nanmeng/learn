def reverseSentence(S, lo, hi):
	# reverse the sentence starting from lo to hi
	if lo >= hi:
		return
	# switch the items at lo and hi
	temp = S[lo]
	S[lo] = S[hi]
	S[hi] = temp
	# reverse the rest part of the sentence
	reverseSentence(S, lo+1, hi-1)

if __name__ == '__main__':
	S = 'this is a test'
	print S
	s = list(S)
	reverseSentence(s, 0, len(s)-1)
	print ''.join(s)
