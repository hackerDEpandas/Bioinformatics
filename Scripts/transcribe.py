from datetime import datetime
start_time = datetime.now()
genome = open('rosalind_dna.txt')
genome_string = genome.read()
string = genome_string.replace('\n', '')
print string
"""
def transcribe(string, letter):
	for i in string:
		if i != 'T':
"""
