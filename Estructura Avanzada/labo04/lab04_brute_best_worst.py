import matplotlib.pyplot as plt
import math, random, time 
import kmp as kmp
import brute_pattern as bp
import numpy as np



def kmp_time(pat,txt):
	start = time.clock()
	kmp.KMPSearch(pat,txt)
	end = time.clock()
	result = end - start
	return result

def brute_time(pat,txt):
	start = time.clock()
	bp.brute_pattern(pat,txt)
	end = time.clock()
	result = end - start
	return result



kmp_times_txt1 = []
kmp_times_txt2 = []
kmp_times_txt3 = []
kmp_times_txt4 = []


txt_size = 1000000
exp_repeat_times = 10

# Caso 1: palabras iguales co un k = 7
pat1 = "blaquen"
txt1 = pat1*txt_size
print(len(txt1))

for i in range(exp_repeat_times):
	kmp_times_txt1.append(brute_time(pat1,txt1))

# Caso 2: n "palabras" iguales
pat2 = "b"
txt2 = pat2*txt_size*len(pat1)
print(len(txt2))

for i in range(exp_repeat_times):
	kmp_times_txt2.append(brute_time(pat2,txt2))

# Caso 3: una "palabra" igual al texto
pat3 = "b"*txt_size*len(pat1)
txt3 = pat3
print(len(txt3))

for i in range(exp_repeat_times):
	kmp_times_txt3.append(brute_time(pat3,txt3))

# Caso 4 palabras iguales con un k = 18
pat4 = "blaquenaitormaster"
txt4 = pat4*txt_size
txt4 = txt4[:len(txt3)]
print(len(txt4))

for i in range(exp_repeat_times):
	kmp_times_txt4.append(brute_time(pat4,txt4))


plot = [i for i in range(10)]
kmp_np = np.array(kmp_times_txt1)
plt.plot(plot,kmp_times_txt1)
plt.plot(plot,kmp_times_txt2)
plt.plot(plot,kmp_times_txt3)
plt.plot(plot,kmp_times_txt4)
# plt.plot([1,2,3,4,5,6],brute_times)

# plt.show()
plt.title('Brute Pattern Matching Algorithm')

plt.ylabel('Tiempo (s)')
plt.xlabel('Iteration')
plt.legend([
	'Caso 1',
	'Caso 2',
	'Caso 3',
	'Caso 4'
	# 'Brute Force'
	], loc='upper left')
plt.show()