import radix_sort
import math, random, time 
from algorithms.sorting import quick_sort
import matplotlib.pyplot as plt

test_list = []

quick_times = []
radix_times = []

test_size = [10, 100, 1000]


for size in test_size:

	for x in range(0,size):
		new_val=random.randint(math.pow(10,4), math.pow(10,5))
		test_list.append(new_val)

	#print(test_list)

	start = time.clock()
	quick_sort.sort(test_listlist)
	end = time.clock()
	result_quick = end - start
	quick_times.append(result_quick)
	#print ("quick: {}".format(result_quick))

	start = time.clock()
	radix_sort.radixSort(test_list)
	end = time.clock()
	result_radix = end - start
	radix_times.append(result_radix)
	#print ("radix: {}".format(result_radix))

plot = []

for i in range(0, len(quick_times) ):
	plot.append(i)

plt.title('Analisis Experimental')
plt.plot(plot,radix_times)
plt.plot(plot,quick_times)
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamano (10^n)')
plt.legend(['radix sort', 'quick sort'], loc='upper left')
plt.show()