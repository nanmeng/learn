from collections import deque

def addOneToDigitStream(S):
	# S is a stream of digits
	# add 1 to it and return the result
	if len(S) <= 0:
		return None
	Q = deque([])
	for d in S:
		Q.appendleft(d)
	print Q
	power = 0
	base = 10
	digit = Q.popleft()
	# print digit,
	remain = (digit + 1) % base
	carry = (digit + 1) / base
	total = remain
	# print total
	while True:
		try:
			power += 1
			digit = Q.popleft()
			# print base ** power
			# print digit,
			remain = (digit + carry) % base
			carry = (digit + carry) / base
			total += remain * (base ** power)
			# print total
		except:
			break
	if carry > 0:
		total += carry * (base ** power)
	return total

if __name__ == '__main__':
	S = [8,7,8,9,9,9]
	print addOneToDigitStream(S)
	S = [9,9,9,9,9,9,9,9,9,9,9,9,9]
	print addOneToDigitStream(S)
