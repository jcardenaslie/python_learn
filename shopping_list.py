import os

def show_list():
	clear_screen()
	if len(shopping_list) < 1:
		print("- The list is empty\n")
	else:
		print("\nYour current shopping list:")
		index = 1
		for item in shopping_list:
			print("{}. {}".format(index,item))
			index += 1
		print("-"*10)

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def help():
	clear_screen()
	print("""
	Enter the item name to add it to the list, 
	Enter 'DONE' to finish,
	Enter 'HELP' for Instructions,
	Enter 'LIST' to see the current list,
	ENTER 'SAVE' to save the list
	Enter 'LOAD' to load previous list
	Enter 'REMOVE' to remove previous list
		""")

def add_to_list(new_item):
	show_list()
	
	if len(shopping_list):
		position = input("Where should I add {}?\n"
			"Press ENTER to add to the end of the list\n"
			"> ".format(new_item))
	else:
		position = 0	
	
	try:
		position = abs(int(position))
	except ValueError:
		position = None

	if position is not None:
		shopping_list.insert(position - 1, new_item)
	else:
		shopping_list.append(new_item)
	# print("Added {} ".format(new_item) + "item count {}".format(len(shopping_list)))
	show_list()

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

def remove_form_list():
	show_list()

	item_to_remove = input("What would you like to remove?"
		"> ")
	
	try:
		shopping_list.remove(item_to_remove)
	except ValueError:
		pass
	show_list()

shopping_list = []

print("New Shopping List")
help()

while True:
	new_item = input("> ")

	if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
		break
	elif new_item.upper() == 'HELP':
		help()
		continue
	elif new_item.upper() == 'LIST':
		show_list()
		continue
	elif new_item.upper() == "SAVE" :
		save_list(shopping_list)
		continue
	elif new_item.upper() == "LOAD" :
		shopping_list = load_list()
		continue
	elif new_item.upper() == 'REMOVE':
		remove_form_list()
		continue
	add_to_list(new_item)

show_list()