import random
import os
import sys
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

keep_playing = True

def welcome():
	start = input("Press enter/return to start or Q to quit").lower()
	if start == 'q':
		print('Bye')
		sys.exit()
	else:
		return True

def clear_screen():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')

def draw_game(guesses, display_game_string):
	# draw spaces
	print("Guesses left: {}".format(guesses))
	print("\n")
	print("Guess a letter")
	print(display_game_string)

def test_for_int(guess_letter):
	try:
		test_for_int = int(guess_letter)
	except ValueError:
		return True
	else:
		return False

def test_for_letter(guess_letter):
	if len(guess_letter) < 2 and len(guess_letter) > 0:
		return True
	else:
		return False
		
def try_guess(guess_letter, list_solution_word, display_game_string ):
	if guess_letter in list_solution_word:
		index = 0
		for letter in list_solution_word:
			if guess_letter == letter:
				list_game_string = list(display_game_string.split(" "))
				list_game_string[index] = guess_letter
				display_game_string = " ".join(list_game_string)
			index += 1
		return display_game_string
	else:
		# bad_guesses.append(guess_letter)
		return display_game_string

def play(keep_playing):
	welcome()
	while keep_playing:
		
		random_pick = random.randint(0, len(list_words) - 1)
		random_word = list_words[random_pick]

		bad_guesses = []

		list_solution_word = list(random_word)
		blank_builder = "_"*len(random_word)
		blank_list = list(blank_builder)
		display_game_string = " ".join(blank_list)

		guesses = 12
		game_solution_string = "".join(list_solution_word)
		
		while guesses:
			clear_screen()
			draw_game(guesses, display_game_string)

			guesses -= 1
			# clear_screen()
			# take a guessS
			guess_letter = input("> ").lower()
			
			if test_for_int(guess_letter) and test_for_letter(guess_letter):
				display_game_string = try_guess(guess_letter, list_solution_word, display_game_string)
			else:
				print("That's not a letter")

			my_solution_string = "".join(display_game_string.split(" "))

			if my_solution_string == game_solution_string:
				print("\nGame Won! Congratulations")
				print(display_game_string)
				break
		else:
			print("Game Lost, no more guesses left :(")

		if input("\nWanna play again Y/n ?").lower() != 'y':
			keep_playing = False

play(keep_playing)