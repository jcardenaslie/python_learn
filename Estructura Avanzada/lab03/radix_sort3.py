#En general este codigo difiera de la implementacion vista en geeksforgeeks
#este algoritmo no recupera los indices ni almacena la cantidad de ocurrencias
#en la lista temporal, sino que almacena directamente los valores ordenados.
#en los indices
import random
iterations = 0

def radix_sort(random_list):
    
    len_random_list = len(random_list)
    modulus = 10
    div = 1 #digito divisor o K
    
    #counting sort
    while True:
        global iterations 
        iterations += 1
        # Array bidimensional que guarda los valores en los indices entre 0 y 9
        new_list = [[], [], [], [], [], [], [], [], [], []]
        
        #O(n)
        for value in random_list:
            least_digit = value % modulus #valor menos significativo del orden de modulus
            least_digit /= div #indice en new_list
            new_list[int(least_digit)].append(value) # insercion en arreglo transitivo
        
        modulus = modulus * 10 # hace crecer el valor para luego fijarse en el sgte valor menos significativo
        div = div * 10

        # si el tamaño de esta sub lista es igual al tamaño de la lista original. Aqui se detiene
        if len(new_list[0]) == len_random_list:
            return new_list[0]

        random_list = []
        rd_list_append = random_list.append
        
        # pasa los valores de forma ordenada a randomlist para seguir iterando
        for x in new_list:
            for y in x:
                rd_list_append(y)



# # random_data = [13, 8, 1992, 31, 3, 1993]
# random_data = [ 170, 45, 75, 90, 802, 24, 2, 66]
# # random_data = [random.randint(0, 1000000) for i in range(0,1000)]
# arr = []
# arr = radix_sort(random_data)
# # print(arr)
# print("iterations {}".format(iterations))