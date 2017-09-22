import radix_sort2
import radix_sort3
import math, random, time 
from algorithms.sorting import quick_sort
from algorithms.sorting import bubble_sort
from algorithms.sorting import heap_sort
from algorithms.sorting import insertion_sort
from algorithms.sorting import merge_sort
from algorithms.sorting import selection_sort
import matplotlib.pyplot as plt

def radix_time(test_list):
	# RADIX SORT
	start = time.clock()
	radix_sort3.radix_sort3(test_list)
	end = time.clock()
	result_radix3 = end - start
	return result_radix3
	# times_radix3.append(result_radix3)

def quick_time(test_list):
	#QUICK SORT
	start = time.clock()
	quick_sort.sort(test_list)
	end = time.clock()
	result_quick = end - start
	return result_quick

times_quick = []
times_radix = []
times_bubble = []
times_heap = []
times_insertion = []
times_selection = []

test_size = [1, 10, 100, 1000, 10000, 100000, 1000000]
test_size2 = [1000, 2000, 3000, 4000]

iter_lenght = len(test_size)

for size in test_size:
	test_quick = []
	test_radix = []
	test_bubble = []
	test_heap = []
	test_insertion = []
	test_selection = []

	for x in range(0,size):
		new_val=random.randint(math.pow(10,4), math.pow(10,5))
		test_quick.append(new_val)
		test_radix.append(new_val)
		test_bubble.append(new_val)
		test_heap.append(new_val)
		test_insertion.append(new_val)
		test_selection.append(new_val)

	
	times_quick.append(quick_time(test_quick))
	times_radix.append(radix_time(test_radix))
	


plot = []

for i in range(0,iter_lenght):
	# print ("radix: {}".format(times_radix[i]))
	print ("radix 3: {}".format(times_radix[i]))
	print ("quick: {}".format(times_quick[i]))
	# print ("quick 2: {}".format(times_quick2[i]))
	print("\n")


for i in range(0, len(times_quick) ):
	plot.append(i)

plt.title('Analisis Experimental')
plt.plot(plot,times_quick)
# plt.plot(plot,times_quick2)
# plt.plot(test_size2,times_radix)
plt.plot(plot,times_radix)
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamano (10^n)')
plt.legend([
	'quick sort',
	# 'quick sort 2' 
	# 'radix sort', 
	'radix_sort'
	], loc='upper left')
plt.show()
