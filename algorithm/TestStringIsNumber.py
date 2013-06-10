def testStringIsNumber(S):
	# given a string, test if it is a number radix 10 only
	valid = {
			'0':True,
			'.':False}
	for i in xrange(1, 10):
		valid[str(i)] = True

	S = list(S)
	if len(S) == 0:
		return False
	if S[0] == '+' or S[0] == '-':
		del S[0]
	if len(S) == 0:
		return False
	need_digit = False
	for i in xrange(0, len(S)):
		if not valid.has_key(S[i]) or not valid[S[i]]:
			return False
		if i == 0:
			if S[i] == '0':
				for i in xrange(0,10):
					valid[str(i)] = False
			valid['.'] = True
		if i == 1:
			for i in xrange(1,10):
				valid[str(i)] = True
		if not valid['0'] and i > 0:
			valid['0'] = True
		if need_digit:
			for x in xrange(0,10):
				if S[i] == str(x):
					need_digit = False
		if S[i] == '.':
			# can seen dot only once
			valid['.'] = False
			# we need to see at least another digit after dot
			need_digit = True
	if need_digit:
		return False
	return True

if __name__ == '__main__':
	S = [
			'1234567890',
			'+1234567890',
			'-1234567890',

			'0.123456789',
			'+0.123456789',
			'-0.123456789',

			'0.000000000',
			'+0.000000000',
			'-0.000000000',

			'0.000000001',
			'+0.000000001',
			'-0.000000001',

			'1234551.002103',
			'+1234551.002103',
			'-1234551.002103',
			]
	for s in S:
		print testStringIsNumber(s)
	print '----'
	S = [
			'',
			'0123456789',
			'+',
			'-',
			'+++++',
			'-----',
			'1234551.002103x',
			'+1234551.002103x',
			'-1234551.002103x',
			'-12.34551.002103x',
			'-1234551002103.',
			'-1234551002103..',
			]
	for s in S:
		print testStringIsNumber(s)
