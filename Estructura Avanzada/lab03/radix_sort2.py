import math, random, time 
from algorithms.sorting import quick_sort
import matplotlib.pyplot as plt
import radix_sort

def countingSort(arr, exp1):
 
    n = len(arr)
 
    output = [0] * (n)
 
    count = [0] * (10)
 
    for i in range(0, n):
        index = int(arr[i]/exp1)
        count[ (index)%10 ] += 1
 
    for i in range(1,10):
        count[i] += count[i-1]
 
    i = n-1
    while i>=0:
        index = int(arr[i]/exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1
 
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
 
def radixSort2(arr):
 
    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10

# arr = []

# test_size = [1, 10, 100, 1000]
# test_size2 = [1000, 2000, 3000, 4000]


# radix_times = []

# for size in test_size:

#     for x in range(0,1000):
#             new_val=random.randint(math.pow(10,4), math.pow(10,5))
#             arr.append(new_val)

#     start = time.clock()
    
#     radix_sort.radixSort(arr)
#         # radixSort2(arr)

#     end = time.clock()
#     result_radix = end - start
#     radix_times.append(result_radix)
#     print ("radix: {}".format(result_radix))


# plot = []

# for i in range(0, len(radix_times) ):
#     plot.append(i)

# plt.title('Analisis Experimental')
# plt.plot(test_size2,radix_times)
# plt.ylabel('Tiempo (s)')
# plt.xlabel('Tamano (10^n)')
# plt.legend(['radix sort'], loc='upper left')
# plt.show()
 
