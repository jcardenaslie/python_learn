import radix_sort2 as radix_g4g
# import radix_sort3
import math, random, time 
from algorithms.sorting import quick_sort
from algorithms.sorting import heap_sort
from algorithms.sorting import merge_sort
import matplotlib.pyplot as plt

def radix_time(test_list):
	start = time.clock()
	radix_g4g.radix_sort(test_list)
	end = time.clock()
	result = end - start
	return result

def quick_time(test_list):
	start = time.clock()
	quick_sort.sort(test_list)
	end = time.clock()
	result = end - start
	return result

def heap_time(test_list):
	start = time.clock()
	heap_sort.sort(test_list)
	end = time.clock()
	result = end - start
	return result

def merge_time(test_list):
	start = time.clock()
	heap_sort.sort(test_list)
	end = time.clock()
	result = end - start
	return result


times_quick = []
times_radix = []
times_heap = []
times_merge = []

# test_size = [1, 10, 100, 1000, 10000, 100000, 1000000]
test_size = [1, 10, 100, 1000]
# test_size = [1, 10]
# test_size = [1000, 2000, 3000, 4000]

iter_lenght = len(test_size)

for size in test_size:
	test_data = []

	for x in range(0,size):
		new_val=random.randint(math.pow(10,4), math.pow(10,5))
		# new_val=random.randint(math.pow(10,1), math.pow(10,x+1))
		test_data.append(new_val)

	times_quick.append(quick_time(test_data))
	times_radix.append(radix_time(test_data))
	times_heap.append(heap_time(test_data))
	times_merge.append(merge_time(test_data))


plot = []

for i in range(0, iter_lenght):
	plot.append(i)

plt.title('Analisis Experimental Radix GeekforGeeks')
plt.plot(plot,times_quick)
plt.plot(plot,times_radix)
plt.plot(plot,times_merge)
plt.plot(plot,times_heap)
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamano (10^n)')
plt.legend([
	'quick sort',
	'radix_sort',
	'merge_sort',
	'heap_sort'
	], loc='upper left')
plt.show()
