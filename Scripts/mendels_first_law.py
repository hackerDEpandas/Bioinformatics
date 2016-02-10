from datetime import datetime
start_time = datetime.now()
x = open('rosalind_iprb.txt')
y = x.read().split()

hom = int(y[0])*1.0
het = int(y[1])*1.0
rec = int(y[2])*1.0 

def choose(m, n):
	return (m*(m-1))/n

prob_rec_rec = choose(rec, 2)/choose((hom+het+rec), 2)
prob_het_het = choose(het, 2)/choose((hom+het+rec), 2)
prob_het_rec = (het * rec)/choose((hom+het+rec), 2)

print 1 - (prob_rec_rec + (prob_het_het * 0.25) + (prob_het_rec * 0.5))
print datetime.now() - start_time
