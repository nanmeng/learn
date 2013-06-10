if __name__ == '__main__':

	stack = []
	print stack

	try:
		stack.pop()
	except Exception as e:
		print e

	stack.append(3)
	stack.append(4)
	stack.append(5)

	print stack
