class transcribe_DNA(object):

	def __init__(self, dna):

		self.dna = list(dna)
		self.rna = []

	def generate_RNA(self):

		for i in xrange(len(self.dna)):
			
			if self.dna[i] != 'T':
				self.rna.append(self.dna[i])
			else:
				self.rna.append('U')

		return self.rna


	def test_DNA(self):

		if list(set(self.dna)) == ['A', 'C', '\n', 'T', 'G']:
      			return True
		else:
      			return False

genome = open('nucleotide.txt')
genome_string = genome.read()
instance = transcribe_DNA(genome_string)
test_dna = instance.test_DNA()

if test_dna == True:
	rna_string = instance.generate_RNA()
	print ''.join(rna_string)
