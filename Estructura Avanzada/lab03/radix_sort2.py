import math, random, time 
from algorithms.sorting import quick_sort
import matplotlib.pyplot as plt
import radix_sort

iterations = 0
def countingSort(arr, exp1):
    
    global iterations 
    iterations += 1
    
    n = len(arr)
 
    output = [0] * (n)
 
    count = [0] * (10)
    
    # O(n) suma ocurrencias por indice
    for i in range(0, n):
        index = int(arr[i]/exp1)
        count[ (index)%10 ] += 1
    
    # O(1) suma ocurrencias acumuladas
    for i in range(1,10):
        count[i] += count[i-1]
 
    # O(n) llena el output con un nuevo orden desde count
    # y substrae ocurrencias desde count
    # count da el indice de output
    i = n-1
    while i>=0:
        index = int(arr[i]/exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1
 
    i = 0

    # O(n)
    for i in range(0,len(arr)):
        arr[i] = output[i]
 
def radix_sort(arr):

    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10

# arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
# # arr= [random.randint(0, 100000) for i in range(0,1000)]

# radix_sort(arr)

# print("iterations {}".format(iterations))
# print(arr)

# for i in range(len(arr)):
#     print(arr[i]),
 
 
