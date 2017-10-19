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


kmp_times_txt1 = []
kmp_times_txt2 = []
kmp_times_txt3 = []
kmp_times_txt4 = []

# exp 1 n letras iguales
pat = "b"
txt = pat*j
exp_repeat_times = 10

for i in range(exp_repeat_times):
	kmp_times.append(kmp_time())

# exp 1 letras iguales
pat = "b"
txt = pat*j
exp_repeat_times = 10

for i in range(exp_repeat_times):
	kmp_times.append(kmp_time())


plot = []
kmp_np = np.array(kmp_times)
plt.plot([1:11],kmp_times_txt1)
# plt.plot([1,2,3,4,5,6],brute_times)

# plt.show()
plt.title('String Pattern algorithms')

plt.ylabel('Tiempo (s)')
plt.xlabel('pattern size * (10^n)')
plt.legend([
	'KMP',
	# 'Brute Force'
	], loc='upper left')
plt.show()