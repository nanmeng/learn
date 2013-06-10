import sys

def leftRightJustify(words, width):
	# print words as a paragraph with (width) width
	# each line shall be left and right justified
	i = 0
	while i < len(words):
		w_len = len(words[i])
		if w_len > width:
			print
			print 'ABORT: CANNOT CONTAIN WORD:'
			print words[i]
			return
		# current length of line
		c_len = 0
		line = []
		n_space = width
		n_words = 0
		while c_len + w_len <= width:
			line.append(words[i])
			# current length shall contain a space for a whitespace
			# print 'c_len:', c_len
			# print 'n_words:', n_words
			c_len += w_len+1
			n_words += 1
			i += 1
			if not (i < len(words)):
				break
			w_len = len(words[i])
			if w_len > width:
				print
				print 'ABORT: CANNOT CONTAIN WORD:'
				print len(words[i])
				print words[i]
				return
		# print 'c_len:', c_len
		# print 'n_words:', n_words
		# we added n_words number of extra whitespaces in the length
		n_space = width - c_len + n_words
		# at least put this number of spaces between two words
		if n_words == 1:
			n_space_each = 0
		else:
			n_space_each  = n_space / (n_words-1)
		# if we equally distribute all spaces inbetween the words
		# how many extra spaces we are left with
		if n_words == 1:
			n_extra_space = 0
		else:
			n_extra_space = n_space % (n_words-1)
		# print n_space
		# print n_space_each
		# print n_extra_space

		# print the line
		# print line
		for n in xrange(0, len(line)):
			# print line[n],
			sys.stdout.write(line[n])
			# print ' ' * n_space_each,
			sys.stdout.write(' ' * n_space_each)
			if n_extra_space > 0:
				sys.stdout.write(' ')
				# print ' ',
				n_extra_space -= 1
		print

if __name__ == '__main__':
	words = "In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since. 'Whenever you feel like criticizing any one,' he told me, 'just remember that all the people in this world haven't had the advantages that you've had.' He didn't say any more, but we've always been unusually communicative in a reserved way, and I understood that he meant a great deal more than that. In consequence, I'm inclined to reserve all judgments, a habit that has opened up many curious natures to me and also made me the victim of not a few veteran bores. The abnormal mind is quick to detect and attach itself to this quality when it appears in a normal person, and so it came about that in college I was unjustly accused of being a politician, because I was privy to the secret griefs of wild, unknown men. Most of the confidences were unsought - frequently I have feigned sleep, preoccupation, or a hostile levity when I realized by some unmistakable sign that an intimate revelation was quivering on the horizon; for the intimate revelations of young men, or at least the terms in which they express them, are usually plagiaristic and marred by obvious suppressions. Reserving judgments is a matter of infinite hope. I am still a little afraid of missing something if I forget that, as my father snobbishly suggested, and I snobbishly repeat, a sense of the fundamental decencies is parcelled out unequallyiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii at birth. unequallyiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii".split(' ')
	# print words
	print '11111000001111100000111110000011111000001111100000'
	leftRightJustify(words, 50)
