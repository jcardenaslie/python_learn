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
		# test_radix.append(new_val)
		# test_bubble.append(new_val)
		# test_heap.append(new_val)
		# test_insertion.append(new_val)
		# test_selection.append(new_val)

	
	times_quick.append(quick_time(test_quick))
	times_radix.append(radix_time(test_quick))
	# times_heap.append(heap_time(test_quick))
	



# for i in range(0,iter_lenght):
# 	# print ("radix: {}".format(times_radix[i]))
# 	print ("radix 3: {}".format(times_radix[i]))
# 	# print ("quick: {}".format(times_quick[i]))
# 	# print ("quick 2: {}".format(times_quick2[i]))
# 	print("\n")

plot = []

for i in range(0, iter_lenght):
	plot.append(i)

plt.title('Analisis Experimental Radix G4G')
plt.plot(plot,times_quick)
plt.plot(plot,times_radix)
# plt.plot(plot,times_bubble)
# plt.plot(plot,times_heap)
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamano (10^n)')
plt.legend([
	'quick sort',
	'radix_sort',
	# 'bubble_sort',
	# 'heap_sort'
	], loc='upper left')
plt.show()
