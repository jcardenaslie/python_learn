import sys

def most_frequent(q):

	key = []
	key_occ = [0]*len(q)
	for nro in q:
		if nro in key:
			i = key.index(nro)
			key_occ[i]+=1
		else:
			key.append(nro)
			i = key.index(nro)
			key_occ[i]+=1
	max_val = max(key_occ)
	return max_val


f = open(sys.argv[1], "r")

queries = []
rl = 0
inp = []
#Read input
for line in f:
	if rl == 1:
		leni = line.split(" ")
		for l in leni:
			inp.append(int(l))
	elif rl > 1:
		leni = line.split(" ")
		query = []
		for l in leni:
			query.append(int(l))
		queries.append(query)
	rl += 1

output = []

#Process queries
for q in queries:
	if len(q) == 1: break 
	q_s = inp[q[0]-1:q[1]]
	output.append(most_frequent(q_s))

for o in output:
	print(o)