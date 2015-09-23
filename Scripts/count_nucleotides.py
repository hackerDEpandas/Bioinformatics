class count_nucleotides(object):

	def __init__(self, string):

		self.string = string
		self.count_A = 0
		self.count_C = 0
		self.count_T = 0
		self.count_G = 0

	def counter(self):
		for letter in self.string:
			if letter == 'A':
				self.count_A += 1
			elif letter == 'C':
				self.count_C += 1
			elif letter == 'T':
				self.count_T += 1
			else:
				self.count_G += 1
		return self.count_A, self.count_C, self.count_T, self.count_G

def testStr(string):
	if list(set(string)) == ['A', 'C', 'T', 'G']:
		return True
	else:
		return False

while True:
    genome = raw_input()
    if testStr(genome) == False:
        print('PLEASE USE ONLY CAPITAL LETTERS "A", "C", "T", OR "G".')
        continue
    else:
        break

instance = count_nucleotides(genome)
a_tuple = instance.counter()

print ' A: %d\n C: %d\n T: %d\n G: %d' %(a_tuple[0],a_tuple[1],a_tuple[2],a_tuple[3])
