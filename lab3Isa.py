import matplotlib.pyplot as plt
from math import exp, expm1
from random import randint
import time
from algorithms.sorting import quick_sort

def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n) # arreglo que tendra la solucion ordenada
    
    count = [0] * (10) #arreglo transitivo para contar elementos
    
    #almacena ocurrencias en el arreglo transitivo, las cuenta
    for i in range(0, n):
        index = int(arr[i]/exp1) # divide el numero por el exp = 1, 10 , 100, ...
        count[ (index)%10 ] += 1
    
    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array

    #Suma acumulada del arreglo
    for i in range(1,10):
        count[i] += count[i-1]
    # Build the output array
    
    i = n-1
    while i>=0:
        
        valor_unitario = int(arr[i]/exp1) # se trunca para que no queden los decimales
        
        indice_arr_transitivo = valor_unitario%10
        
        valor_acumulado = count[indice_arr_transitivo]
        
        indice_arr_output = valor_acumulado - 1
        
        output[indice_arr_output] = arr[i]
        
        count[indice_arr_transitivo] -= 1

        #output[ count[ (index)%10 ] - 1] = arr[i] 
        #count[ (index)%10 ] -= 1 # resta 1 a la cuenta acumulada en el arreglo transitivo
        i -= 1
    
    #pasa la solucion al arreglo inicial
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
# Method to do Radix Sort
def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10

r = list()
q = list()
for i in range(1,6):

	test=list(range(pow(10,i)))
	for x in range(0,pow(10,i)):
		test[x]=randint(pow(10,i-1), pow(10,i))

	print(test)


	start = time.clock()
	quick_sort.sort(test)
	end = time.clock()
	print ("quick: ")
	print (end - start)
	q.append(end-start)


	start = time.clock()
	radixSort(test)
	end = time.clock()
	print ("radix: ")
	print (end - start)
	r.append(end-start)
print("r: "),
print(r)
print("q: "),
print(q)


plt.title('Analisis Experimental')
plt.plot([1,2,3,4,5],r)
plt.plot([1,2,3,4,5],q)
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamano (10^n)')
plt.legend(['r', 'q'], loc='upper left')
plt.show()