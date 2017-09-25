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
 
arr = [10, 5, 10.000, 5.000]

countingSort(arr);

print(arr)