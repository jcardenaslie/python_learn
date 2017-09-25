import radix_sort2 as radix_g4g
import radix_sort3 as radix_git
import math, random, time 
from algorithms.sorting import quick_sort
from algorithms.sorting import heap_sort
from algorithms.sorting import merge_sort
import matplotlib.pyplot as plt

def g4g_time(test_list):
	start = time.clock()
	radix_g4g.radix_sort(test_list)
	end = time.clock()
	result = end - start
	return result

def git_time(test_list):
	start = time.clock()
	radix_git.radix_sort(test_list)
	end = time.clock()
	result = end - start
	return result

times_radix_git = []
times_radix_g4g = []

# test_size = [1, 10, 100, 1000, 10000, 100000, 1000000]
# test_size = [1, 10, 100, 1000, 10000, 100000]
# test_size = [1, 10, 100, 1000, 10000]
# test_size = [1, 10, 100, 1000]
test_size = [1, 10, 100]
# test_size = [1, 10]
# test_size = [1000, 2000, 3000, 4000]


iter_lenght = len(test_size)

for size in test_size:
	test_data = []

	for x in range(0,size):
		new_val=random.randint(math.pow(10,1), math.pow(10,3))
		test_data.append(new_val)

	# print(test_data)
	# test_data = [1, 4, 1, 2, 7, 5, 2]

	times_radix_git.append(git_time(test_data))
	times_radix_g4g.append(g4g_time(test_data))


# print(test_data)
plot = []

for i in range(0, iter_lenght):
	plot.append(i)


plt.title('Analisis Experimental Radix G4G vs Otro')
plt.plot(plot,times_radix_git)
plt.plot(plot,times_radix_g4g)
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamaño (10^n)')
plt.legend([
	'otro',
	'g4g',
	], loc='upper left')
plt.show()
