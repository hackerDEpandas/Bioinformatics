from datetime import datetime
start_time = datetime.now()
data = open('rosalind_gc.txt')
data_string = data.read()

ids = []
dna = []
dna_clean = []

for i in data_string.split('>'):
	if i[0:9] == 'Rosalind_':
		ids.append(i[0:13])
		dna.append(i[13:len(i)].replace('\n', ''))
for i in dna:
	dna_clean.append((float(i.count('G'))+float(i.count('C')))/len(i)*100)

print dna_clean
print ids
print datetime.now() - start_time
