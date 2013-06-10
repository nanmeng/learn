def _s(L):
	return ''.join(L)

def seperateWordsWithSpaces(S, D):
	print 'S:', S
	# given string S and dictionary D
	# break S into words that can be found in D
	# then seperate the words with spaces and print out
	word = _s(S)
	if D.has_key(word):
		return [word]

	for i in xrange(1, len(S)):
		word = _s(S[0:i])
		print word
		if D.has_key(word):
			sentence = seperateWordsWithSpaces(S[i:], D)
			if sentence != False:
				sentence = [word] + sentence
				return sentence
			else:
				i += 1
	return False

if __name__ == '__main__':
	S = list('iamastudentfromwaterloo')
	D = {
			'from':1,
			'waterloo':1,
			'hi':1,
			'am':1,
			'yes':1,
			'i':1,
			'a':1,
			'student':1,
			}
	print seperateWordsWithSpaces(S, D)
