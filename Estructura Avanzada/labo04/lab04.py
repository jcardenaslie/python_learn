import matplotlib.pyplot as plt
import math, random, time 
import kmp as kmp
import brute_pattern as bp
import numpy as np



def kmp_time():
	start = time.clock()
	kmp.KMPSearch(pat,txt)
	end = time.clock()
	result = end - start
	return result

def brute_time():
	start = time.clock()
	bp.brute_pattern(pat,txt)
	end = time.clock()
	result = end - start
	return result

test_size = [10, 100, 1000, 10000, 100000, 1000000]


kmp_times = []
brute_times = []

for j in test_size:
	pat = "bla"
	txt = pat*j

	kmp_mean = 0
	brute_mean = 0
	for i in range(0,5):
		kmp_mean +=kmp_time()
		brute_mean +=brute_time()
	kmp_times.append(kmp_mean/5)
	brute_times.append(brute_mean/5)

plot = []
kmp_np = np.array(kmp_times)
plt.plot([1,2,3,4,5,6],kmp_times)
plt.plot([1,2,3,4,5,6],brute_times)

# plt.show()
plt.title('String Pattern algorithms')

plt.ylabel('Tiempo (s)')
plt.xlabel('pattern size * (10^n)')
plt.legend([
	'KMP',
	'Brute Force'
	], loc='upper left')
plt.show()