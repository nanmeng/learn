STR = 'abatebbbbetbetcbetbetbetac'
SUB = 'betac'

sub_idx = 0
str_idx = 0

for i in range(0, len(STR)):

	if sub_idx == len(SUB)-1:
		print 'yes'
		break

	print i, str_idx, STR[str_idx], sub_idx, SUB[sub_idx]

	if SUB[sub_idx] == STR[str_idx]:
		str_idx += 1
		sub_idx += 1
	else:
		sub_idx = 0
		if SUB[sub_idx] == STR[str_idx]:
			str_idx += 1
			sub_idx += 1
		else:
			str_idx = i + 1
