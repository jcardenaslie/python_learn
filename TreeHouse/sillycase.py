def sillycase(string):
    my_string = []
    my_string = list(string)
    print(my_string)
    middle = int(len(my_string)/2)
    substring1 = my_string[:middle]
    substring2 = my_string[middle:]
    
    string1 = "".join(my_string[:middle])
    string1 = string1.lower()

    string2 = "".join(my_string[middle:])
    string2 = string2.upper()
    
    ready_list = string1 + string2

    return ready_list

var = sillycase("teamtreehouse")
print(var)