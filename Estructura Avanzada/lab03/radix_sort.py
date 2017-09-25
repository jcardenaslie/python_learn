 
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n) # arreglo que tendra la solucion ordenada
    
    count = [0] * (10) #arreglo transitivo para contar elementos
    
    #almacena ocurrencias en el arreglo transitivo, las cuenta
    for i in range(0, n):
        index = int(arr[i]/exp1) # divide el numero por el exp = 1, 10 , 100, ...
        count[ (index)%10 ] += 1

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

def radix_sort(arr):
    max1 = max(arr) #elemento mas grande del arreglo
    exp = 1 #divisor
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
 
# arr = [ 170, 45, 75, 90, 802, 24, 2, 66]

# radix_sort(arr)
 
# for i in range(len(arr)):
#     print(arr[i]),
 
