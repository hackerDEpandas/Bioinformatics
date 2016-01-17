from datetime import datetime
start_time = datetime.now()
genome = open('rosalind_revc.txt')
genome_string = genome.read()

rev_comp = []
string = genome_string.replace('\n', '')

for i in reversed(string):
	if i == 'A':
		rev_comp.append('T')
	elif i == 'T':
		rev_comp.append('A')
	elif i == 'C':
		rev_comp.append('G')
	else:
		rev_comp.append('C')

print ''.join(rev_comp)
