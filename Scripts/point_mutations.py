from datetime import datetime
start_time = datetime.now()
genomes = open('rosalind_hamm.txt')
genome_strings = genomes.read()

arr = genome_strings.split('\n')
s = arr[0]
t = arr[1]
count = 0
if len(s) == len(t):
	for i in range(len(s)):
		if s[i] != t[i]:
			count += 1
print count
print datetime.now() - start_time
