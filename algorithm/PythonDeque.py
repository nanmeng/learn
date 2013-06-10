from collections import deque

if __name__ == '__main__':
	q = deque()
	print q
	try:
		q.popleft()
	except Exception as e:
		print e
	q = deque(['Eric', 'John', 'Mike'])
	q.append('Tim')
	q.append('Nan')
	q.append('JBurke')
	q.append('SBiddle')
	print q
