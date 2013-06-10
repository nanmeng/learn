def longestSubstringWithTwoUniqueChars(A, lo, hi):
	print 'trying:', A, lo, hi
	if lo >= hi:
		return []
	mid = (lo + hi-1) / 2
	print 'mid', mid

	# for the case across the mid point
	# grow the substring from the middle
	i = mid
	j = mid+1
	uniques = []
	ibreak = False
	jbreak = False
	while i > lo and j < (hi-1):
		print 'uniques:', uniques
		if not ibreak:
			i -= 1
			if not (A[i] in uniques):
				uniques.append(A[i])
			if len(uniques) > 2:
				# item at i breaks unique limit
				ibreak = True
				del uniques[-1]
				i += 1
		if not jbreak:
			j += 1
			if not (A[j] in uniques):
				uniques.append(A[j])
			if len(uniques) > 2:
				# item at j breaks unique limit
				jbreak = True
				del uniques[-1]
				j -= 1
		if jbreak and ibreak:
			break;
	long_M = A[i:j+1]
	print 'cross:', long_M

	long_L = longestSubstringWithTwoUniqueChars(A, lo, mid)
	print 'left:', long_L

	long_R = longestSubstringWithTwoUniqueChars(A, mid+1, hi)
	print 'right:', long_R

	if len(long_M) >= len(long_L) and len(long_M) >= len(long_R):
		return long_M
	if len(long_L) >= len(long_M) and len(long_L) >= len(long_R):
		return long_L
	return long_R


def find_substring(S, k=1):
    if len(S) < 2:
        return S

    charmap = {}        # Track counts for each char
    unique = 0          # Track the number of unique characters
    longest = ''        # Track the longest word
    start, end = 0, 0   # Iteration pointers
    while end < len(S):
        if unique <= k:
            end += 1
            newchar = S[end - 1]
            charmap[newchar] = charmap.get(newchar, 0) + 1
            if charmap[newchar] == 1:
                unique += 1
        else:
            start += 1
            remchar = S[start - 1]
            charmap[remchar] = charmap[remchar] - 1
            if charmap[remchar] == 0:
                unique -= 1
        if len(S[start:end]) > len(longest) and unique <= k:
            longest = S[start:end]
    return longest

if __name__ == '__main__':
	# A = list('aabbcbbbadef')
	# print longestSubstringWithTwoUniqueChars(A, 0, len(A))
	A = 'aabbcbbbadefbbbbbbbbbbbbbbbbbbbbbc'
	print find_substring(A, 2)
	print '---------'
	# A = list('aabbbbbbbcbbbadef')
	# print longestSubstringWithTwoUniqueChars(A, 0, len(A))
	A = 'aabbbbbbbcbbbadef'
	print find_substring(A, 2)

