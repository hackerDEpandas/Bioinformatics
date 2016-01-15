from datetime import datetime
start_time = datetime.now()
genome = open('rosalind_fib.txt')
tup = genome.read().split()

def count_pairs(old, young, k, n):
	result = None
	if n == 1:
		result = young
	else:
		result = count_pairs(young, old * k + young, k, n-1)
	return result

	
print count_pairs(0,1,int(tup[1]), int(tup[0]))
print datetime.now() - start_time
