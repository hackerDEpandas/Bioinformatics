from datetime import datetime
start_time = datetime.now()
genome = open('rosalind_dna.txt')
genome_string = genome.read()

def count(string, letter):
	count = 0
	for i in string:
		if i == letter:
			count += 1
	return count
print count(genome_string, 'A'), count(genome_string, 'C'), count(genome_string, 'G'), count(genome_string, 'T')
print datetime.now()-start_time
