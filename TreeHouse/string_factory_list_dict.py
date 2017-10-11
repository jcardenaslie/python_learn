def string_factory(dict_list):
	new_list = []
	for i in range(0, len(dict_list)):
		template = "Hi, I'm {name} and I love to eat {food}!".format(**dict_list[i])
		new_list.append(template)
	return new_list

values = [{"name": "Michelangelo", "food": "PIZZA"},{"name": "Garfield", "food": "lasagna"}]

arr = string_factory(values)

print(arr)