def changeChar(src, des, idx):
	return src[0:idx] + [des[idx]] + src[idx+1:]

def _s(L):
	return ''.join(L)

def printSourceToDestinationStringTravel(src, des, D, C=None, CW=None, Stack={}):
	# C list: all the indices that have been changed so far
	# CW list: all the words in the changed (traveled) path
	print '-----', _s(src), '->', _s(des)
	print C
	print CW

	for i in xrange(0, len(src)):
		print 'trying index:', i,
		if C is not None and (str(i) in C):
			# this index has been changed before
			print 'tried'
			continue
		print
		test = changeChar(src, des, i)
		print 'trying:', _s(src), '=>', _s(test), '=>', _s(des)
		if _s(test) == _s(des):
			try:
				Stack[_s(C)] = CW
				print '----- ANSWER:'
				print Stack
				print '-----'
				return
			except:
				print 'oops'
				return
		if not D.has_key(_s(test)):
			# this word must be in the dictionary
			continue
		else:
			if C is None:
				C = []
				CW = []
			C.append(str(i))
			CW.append(_s(test))
			printSourceToDestinationStringTravel(test, des, D, C, CW)


if __name__ == '__main__':
	S = list('CAT')
	D = list('DOG')
	Dictionary = {
			'COT':None,
			'DOT':None,
			'COG':None,
			}
	print changeChar(S, D, 0)
	print _s(changeChar(S, D, 0))
	print changeChar(S, D, 1)
	print _s(changeChar(S, D, 1))
	print changeChar(S, D, 2)
	print _s(changeChar(S, D, 2))
	printSourceToDestinationStringTravel(S, D, Dictionary)
