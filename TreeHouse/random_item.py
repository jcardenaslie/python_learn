import random

def random_item(iter):
	index = random.randint(0, len(iter) - 1)
	return iter[index]

var = random_item("string")
print(var)