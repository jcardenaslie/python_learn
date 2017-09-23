#En general este codigo difiera de la implementacion vista en geeksforgeeks
#este algoritmo no recupera los indices ni almacena la cantidad de ocurrencias
#en la lista temporal, sino que almacena directamente los valores ordenados.
#en los indices

def radix_sort(random_list):
    len_random_list = len(random_list)
    modulus = 10
    div = 1 #digito divisor o K
    while True:
        # Array bidimensional que guarda los valores en los indices entre 0 y 9
        new_list = [[], [], [], [], [], [], [], [], [], []]
        
        #esta implementacion es un poco distinta
        for value in random_list:
            least_digit = value % modulus #offset o indice en new_list 10%10 => 0 , va en indice 0
            least_digit /= div #valor menos significativo  0/10 => 0
            new_list[int(least_digit)].append(value) # insercion en arreglo transitivo
        
        modulus = modulus * 10 # hace crecer el valor para luego fijarse en el sgte valor menos significativo
        div = div * 10

        #si la lista esta vacia
        if len(new_list[0]) == len_random_list:
            return new_list[0]

        #vacia random list
        random_list = []
        rd_list_append = random_list.append
        
        #construccion lista solucion, para el indice 0 agrega sus valores ordenados y asi en adelante
        for x in new_list:
            for y in x:
                rd_list_append(y)

# random_data = [13, 8, 1992, 31, 3, 1993]
# random_data = [ 170, 45, 75, 90, 802, 24, 2, 66]
# print(radix_sort3(random_data))