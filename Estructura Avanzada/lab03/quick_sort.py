import radix_sort2
import math, random, time 
from algorithms.sorting import quick_sort
import matplotlib.pyplot as plt

test_list = []
test_list2 = []

quick_times = []

test_size = [1, 10, 100, 1000]
test_size2 = [1000, 2000, 3000, 4000]


for size in test_size:

	for x in range(0,size):
		new_val=random.randint(math.pow(10,4), math.pow(10,5))
		test_list.append(new_val)

	#QUICK SORT
	start = time.clock()
	quick_sort.sort(test_list)
	end = time.clock()
	result_quick = end - start
	quick_times.append(result_quick)

plot = []

for i in range(0, len(quick_times) ):
	plot.append(i)

plt.title('Analisis Experimental')
plt.plot(test_size2,quick_times)
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamano (10^n)')
plt.legend(['quick sort'], loc='upper left')
plt.show()