import radix_sort2
import radix_sort3
import math, random, time 
from algorithms.sorting import quick_sort
import matplotlib.pyplot as plt


times_quick = []
times_quick2 = []
times_radix = []
times_radix3 = []

test_size = [1, 10, 100, 1000, 10000, 100000, 1000000]
test_size2 = [1000, 2000, 3000, 4000]
test_size3 = [1000] * 5

iter_lenght = len(test_size)

for size in test_size:
	test_quick = []
	test_quick2 = []
	test_radix = []
	test_radix2 = []

	for x in range(0,size):
		# new_val=random.randint(math.pow(10,4), math.pow(10,5))
		if x > int(size/2):
			new_val =random.randint(0, int(size/2))
		else:
			new_val =random.randint(int(size/2), size)


		test_quick.append(new_val)
		test_quick2.append(new_val)
		test_radix.append(new_val)
		test_radix2.append(new_val)
	
	#QUICK SORT
	start = time.clock()
	quick_sort.sort(test_quick)
	end = time.clock()
	result_quick = end - start
	times_quick.append(result_quick)

	#RADIX SORT
	# start = time.clock()
	# radix_sort2.radixSort2(test_list2)
	# end = time.clock()
	# result_radix = end - start
	# times_radix.append(result_radix)

	# RADIX SORT
	start = time.clock()
	radix_sort3.radix_sort3(test_radix2)
	end = time.clock()
	result_radix3 = end - start
	times_radix3.append(result_radix3)


plot = []

for i in range(0,iter_lenght):
	# print ("radix: {}".format(times_radix[i]))
	print ("radix 3: {}".format(times_radix3[i]))
	print ("quick: {}".format(times_quick[i]))
	# print ("quick 2: {}".format(times_quick2[i]))
	print("\n")


for i in range(0, len(times_quick) ):
	plot.append(i)

plt.title('Analisis Experimental')
plt.plot(plot,times_quick)
# plt.plot(plot,times_quick2)
# plt.plot(test_size2,times_radix)
plt.plot(plot,times_radix3)
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamano (10^n)')
plt.legend([
	'quick sort',
	# 'quick sort 2' 
	# 'radix sort', 
	'radix_sort3'
	], loc='upper left')
plt.show()