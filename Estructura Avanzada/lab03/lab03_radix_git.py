import radix_sort3 as radix_g4g
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

input_size = [10, 100, 1000, 10000, 100000, 1000000]
# input_size = [10, 100, 1000, 10000, 100000]
# input_size = [10, 100, 1000, 10000]
# input_size = [10, 100, 1000]
# input_size = [10, 100, 1000]
# input_size = [10]
# input_size = [1000, 2000, 3000, 4000]

iter_lenght = len(input_size)

input_range = 4

for size in input_size:
	test_data = []

	for x in range(0,size):
		new_val=random.randint(math.pow(10,1), math.pow(10,input_range))
		# new_val=random.randint(math.pow(10,1), math.pow(10,x+1))
		test_data.append(new_val)

	times_quick.append(quick_time(test_data))
	times_radix.append(radix_time(test_data))
	times_heap.append(heap_time(test_data))
	times_merge.append(merge_time(test_data))


plot = []

for i in range(0, iter_lenght):
	plot.append(i)

for i in range(0,iter_lenght):
	print("q: {0:.7f}".format(times_quick[i]))
	print("m: {0:.7f}".format(times_merge[i]))
	print("h: {0:.7f}".format(times_heap[i]))
	print("r: {0:.7f}".format(times_radix[i]))
	print("")

plt.title('Analisis Experimental Radix Otro')
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
