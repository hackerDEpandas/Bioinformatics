from datetime import datetime
import numpy as np
start_time = datetime.now()
genome = open('rosalind_rna.txt')
genome_string = genome.read()
rna = []
def transcribe(string):
	string = string.replace('\n', '')
	for i in string:
		if i != 'T':
			rna.append(i)
		else:
			rna.append('U')
	return ''.join(rna)

saved = transcribe(genome_string)
print saved
print datetime.now() - start_time
