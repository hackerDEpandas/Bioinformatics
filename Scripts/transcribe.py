from datetime import datetime
import numpy as np
start_time = datetime.now()
genome = open('rosalind_rna.txt')
genome_string = genome.read()
dna = []
def transcribe(string):
	string = string.replace('\n', '')
	for i in string:
		if i != 'T':
			dna.append(i)
		else:
			dna.append('U')
	return ''.join(dna)

saved = transcribe(genome_string)
print saved
print datetime.now() - start_time
