import random

def coinToss():
	return random.randint(1,2)

def dieRoll():
	ret = 7
	while ret > 5:
		bit1 = 1 * (coinToss()-1)
		bit2 = 2 * (coinToss()-1)
		bit4 = 4 * (coinToss()-1)
		ret = bit1 + bit2 + bit4
	return ret

if __name__ == '__main__':
	result = [0,0,0,0,0,0]
	for i in xrange(0,20000000):
		num = dieRoll()
		result[num-1] += 1
	for i in xrange(0, len(result)):
		print result[i]
