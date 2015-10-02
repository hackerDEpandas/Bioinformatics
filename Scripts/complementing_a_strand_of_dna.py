class reverse_DNA(object):

	def __init__(self, dna):
		self.dna = dna
		self.reverse_compliment = []

	def reversed_compliment(self):

		for i in reversed(self.dna):
			
			if i == 'A':
				self.reverse_compliment.append('T')

			elif i == 'T':
				self.reverse_compliment.append('A')

			elif i == 'C':
				self.reverse_compliment.append('G')

			elif i == 'G':
				self.reverse_compliment.append('C')

		return self.reverse_compliment

	def test_DNA(self):

		if list(set(self.dna)) == ['A', 'C', '\n', 'T', 'G']:
			return True

		else:
			return False


genome = open('rosalind_dna.txt')
genome_string = genome.read()
instance = reverse_DNA(genome_string)
test_dna = instance.test_DNA()

if test_dna == True:
	result = instance.reversed_compliment()
	print ''.join(result)

else:
	print 'Make sure the text file you load contains capital letters "A", "T", "C", or "G" only!'
