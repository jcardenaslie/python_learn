import random
#make list of words
list_words=[
	'apple',
	'banana',
	'orange',
	'coconut',
	'strawberry',
	'lime',
	'grapefruit',
	'lemon',
	'kumquat',
	'blueberry',
	'melon'
]
# pick a random word
# simplemente ocupar .choice sobre la lista => random.choice(list)
random_pick = random.randint(0, len(list_words) - 1)
random_word = list_words[random_pick]

list_solution_word = list(random_word)
blank_builder = "_"*len(random_word)
blank_list = list(blank_builder)
display_game_string = " ".join(blank_list)

guesses = 12
game_solution_string = "".join(list_solution_word)

while guesses:

	# draw spaces
	print("\n")
	print("Guess a letter")
	print(display_game_string)

	# take a guessS
	guess_letter = input("> ").lower()
	
	try:
		test_for_int = int(guess_letter)
	except ValueError:
		print("")
	else:
		print("That's a number, try again!")
		continue

	#checking for just a letter
	if len(guess_letter) < 2 and len(guess_letter) > 0:
		#Strike
		if guess_letter in list_solution_word:
			index = 0
			for letter in list_solution_word:
				if guess_letter == letter:
					# draw guessed letters
					list_game_string = list(display_game_string.split(" "))
					list_game_string[index] = guess_letter
					display_game_string = " ".join(list_game_string)
				index += 1
		else:
			print("Wrong letter try again!")
	else:
		print("That's not a letter")

	guesses -= 1

	# I do this cuz game_string contains spaces for display prupouse
	my_solution_string = "".join(display_game_string.split(" "))
	# print out win/lose
	if my_solution_string == game_solution_string:
		print("Game Won! Congratulations")
		print(display_game_string)
		break

else:
	print("Game Lost, no more guesses left :(")
	print("")
