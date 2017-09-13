import random

secret_num = random.randint(1, 10)
number_guesses = 5
not_guessed = True
keep_playing = True

def try_number(guess_num):
	if guess_num == secret_num:
		print("You got it! The number is {}".format(secret_num))
		return False
	else:
		if guess_num > secret_num:
			print("That's too high, try again\n")
		elif guess_num < secret_num:
			print("That's too low, try again\n")
		return True

def restart_game(secret_num, number_guesses, not_guessed):
	secret_num = random.randint(1, 10)
	number_guesses = 5
	not_guessed = True

def game(number_guesses, not_guessed):
	while number_guesses and not_guessed:
		try:
			guess_num = int(input("Guess a number between 1 and 10:"))
		except ValueError:
			print("Thats no a number! try again")
		else:
			number_guesses -= 1
			not_guessed = try_number(guess_num)
			print("Remaining guesses {}".format(number_guesses))
	else:
		print("You run out of guesses :(")

while keep_playing:
	game(number_guesses, not_guessed)
	quit = input("Do you want to keep playing? (enter no to stop)")

	if quit == "no" : 
		keep_playing = False
		print("Bye!")
	else: 
		keep_playing = True
		restart_game(secret_num, number_guesses, not_guessed)
