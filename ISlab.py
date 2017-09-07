import ISsplay
import ISAVL
import time, random
import matplotlib.pyplot as plt

def insert_test(tree, buff):
    s = time.clock()
    for x in buff:
        tree.insert(x)
    e = time.clock()
    return e - s

def search_test(tree, buff):
    s = time.clock()
    for x in buff:
        tree.search(x)
    e = time.clock()
    return e - s

AVL_S=list()
AVL_I=list()
SPLAY_S=list()
SPLAY_I=list()

print("-----------AVL:")
for x in [10, 100, 1000, 10000, 100000]:
    buff = [random.randint(0, 500) for _ in range(x)]
    print (x)
    for tree in [ISAVL.AVLTree]:
        a = tree()
        print ("insert: "),
        AVL_I.append(insert_test(a, buff))
        print ("search: "),
        AVL_S.append(search_test(a,buff))

print("-----------SPLAY:")
for x in [10, 100, 1000, 10000, 100000]:
    buff = [random.randint(0, 500) for _ in range(x)]
    print (x)
    for tree in [ISsplay.Splaytree]:
        a = tree()
        print ("insert: "),
        SPLAY_I.append(insert_test(a, buff))
        print ("search: "),
        SPLAY_S.append(search_test(a, buff))

plt.title('Análisis Experimental')
plt.plot([1,2,3,4,5],AVL_S)
plt.plot([1,2,3,4,5],AVL_I)
plt.plot([1,2,3,4,5],SPLAY_S)
plt.plot([1,2,3,4,5],SPLAY_I)
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamaño (10^n)')
plt.legend(['AVL SEARCH', 'AVL INSERT','SPLAY SEARCH','SPLAY INSERT'], loc='upper left')
plt.show()
