import matplotlib.pyplot as plt
from math import exp, expm1
from random import randint
import time

import BinomialHeap
import BinaryHeap
import random

bino_insert = list()
bina_insert = list()
t1 = 0
t2 = 0
binaHeap = BinaryHeap.BinHeap()
binoHeap = BinomialHeap.BinomialHeap()

for i in range(1,6):
	for x in range(1,pow(10,i)):
		val = randint(pow(10,i-1),pow(10,i))
		start = time.clock()
		n = BinomialHeap.BinomialHeapNode(val)
		BinomialHeap.insert(binoHeap, n)
		end = time.clock()
		t1 += end-start
		start = time.clock()
		binaHeap.insert(val)
		end = time.clock()
		t2 += end-start
	bino_insert.append(t1)
	bina_insert.append(t2)

plt.title('Analisis Experimental')
plt.plot([1,2,3,4,5],bino_insert)
plt.plot([1,2,3,4,5],bina_insert)
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamano (10^k)')
plt.legend(['Binomial Heap: Insert', 'Binary Heap Insert'], loc='upper left')
plt.show()