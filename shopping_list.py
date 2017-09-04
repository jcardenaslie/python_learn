import os

def show_list():
	if len(shopping_list) < 1:
		print("- The list is empty\n")
	else:
		print("\nYour current shopping list:")
		for item in shopping_list:
			print("-" + item)
		print("\n")

def help():
	print("""
Enter the item name to add it to the list, 
Enter 'DONE' to finish,
Enter 'HELP' for Instructions,
Enter 'LIST' to see the current list,
ENTER 'SAVE' to save the list
Enter 'LOAD' to load previous list
	""")

def add_to_list(new_item):
	shopping_list.append(new_item)
	print("Added {} ".format(new_item) + "item count {}".format(len(shopping_list)))

def save_list(list):
	shopping_list = open("C:/Users/joaquin/Desktop/python/foo.txt", "w")
	for item in list:
		shopping_list.write(item + "\n")
	shopping_list.close()

def load_list():
	shopping_list_os = open("C:/Users/joaquin/Desktop/python/foo.txt", "r")
	saved_list = shopping_list_os.read().split('\n')
	list = []
	for item in saved_list:
		if item != "":
			list.append(item) 
	shopping_list_os.close()
	return list



shopping_list = []

print("New Shopping List")
help()

while True:
	new_item = input("> ")

	if new_item == 'DONE' :
		break
	elif new_item == 'HELP':
		help()
		continue
	elif new_item == 'LIST':
		show_list()
		continue
	elif new_item == "SAVE" :
		save_list(shopping_list)
		continue
	elif new_item == "LOAD" :
		shopping_list = load_list()
		continue
	add_to_list(new_item)

show_list()