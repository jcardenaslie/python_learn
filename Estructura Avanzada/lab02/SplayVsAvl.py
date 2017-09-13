import CSplayTree 
import CAvlTree
import random, time 
import matplotlib.pyplot as plot

#Test insert with 10 elements

sp_i = CSplayTree.SplayTree()


for x in range(1,10):
	val_insert = random.randint(1, 100)
	sp_i[val_insert] = val_insert

sp_i.preorder(sp_i.root)