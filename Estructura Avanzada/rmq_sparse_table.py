def preprocesor(lup,arr):
	arr_len = len(arr)
 		for i in range(arr_len):
 			lup[i][0] = i

		 for j in range(1, arr_len + 1):
		  for k in range(arr_len):
		  	t = i + (1<<(j-1))
		    if arr[lup[k][j-1]] < arr[lup[t][j-1]]:
		    	lup[k][j] = lup[k][j-1]
		    else:
		    	lup[k][j] = lup[t][k-1]

def query(lup, arr, L , R):
	int j = int(log2(R-L+1))

	if arr[lup[L][j]] <= arr[lup[R-int(pow(2,j)+1)][j]]:
		return arr[lup[L][j]]
	else:
		return arr[lup[R-int(pow(2,j)+1)][j]]

def RMQ(lup, arr, query):
	q_len = len(query)
	preprocesor(lup,arr)

	for i in range(q_len):
		int L = q[i].L
		int R = q[i].R

		print("Minimum of[{} , {}] is {}".format(L,R,query(lup,arr,L,R)))


a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
n = len(a)
q = [[0, 4], [4, 7], [7, 8]]
m = len(1)
RMQ(a, n, q, m);