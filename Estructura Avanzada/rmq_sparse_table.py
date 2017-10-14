import math
def preprocesor(arr):
	a_len = len(arr)

	lup = [ [0 for i in range(a_len)] for i in range(a_len)]

	for i in range(a_len):
		lup[i][0] = i
	
	j = 1
	while (1<<j) <= a_len:
		i = 0
		while (i + (1<<j) - 1 < a_len):
			k = 1<<(j-1)
			t = i + k
			if arr[lup[i][j-1]] < arr[lup[t][j-1]]:
				lup[i][j] = lup[i][j-1]
			else:
				lup[i][j] = lup[t][j-1]
			i += 1
		j += 1

	return lup

def query(lup, arr, L, R):
	j = int(math.log((R-L+1),2))
	pw = int(math.pow(2,j))
	if arr[lup[L][j]] <= arr[lup[R-pw+1][j]]:
		return arr[lup[L][j]]
	else:
		return arr[lup[R-pw+1][j]]



a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
# a = [18, 17, 13, 19, 15, 11, 20]

queries = [[0, 4], [4, 7], [7, 8]]
lup = preprocesor(a)

print("lookup:")
for l in lup:
	print(l)


for qry in queries:
	L = qry[0]
	R = qry[1]
	result = query(lup,a,L,R)
	print("[{},{}] = {}".format(L,R,result))
	

