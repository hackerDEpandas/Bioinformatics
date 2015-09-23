N = raw_input()

def testStr(string):

	if list(set(string)) != ['A', 'C', 'T', 'G']:
		return False
	else:
		return True

def countNuc(string):

	countA = 0 
	countT = 0
	countC = 0
	countG = 0

	for i in string:
		if i == 'A':
			countA += 1
		elif i == 'T':
			countT += 1
		elif i == 'C':
			countC += 1
		else:
			countG += 1
	return countA, countT, countC, countG

if testStr(N) == True:
	tuples = countNuc(N)
	print ' A: %d\n T: %d\n C: %d\n G: %d' %(tuples[0], tuples[1], tuples[2], tuples[3])
