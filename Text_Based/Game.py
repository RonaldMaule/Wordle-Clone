import random, os

previous_words = []

def Main() -> None:
	Intro()

	play = True
	while play:
		play = Game()
	
	Close()

def Intro() -> None:
	print("Welcome to Wordle!")
	print("How to tell if your guess is correct:")
	print("0 - Letter is incorrect")
	print("1 - Letter is correct but in the wrong place")
	print("2 - Letter is correct and in the correct place")
	print()

	Get_previous_words()

def Game() -> bool:
	correct_word = Get_word()
	Update_previous_words(correct_word)
	correct = False

	guesses = []
	for _ in range(6):
		guess = str(input("Enter guess:\n")).strip()
		print()

		if len(guess) != 5:
			while len(guess) != 5:
				print("Sorry, you can only guess 5 letter words.")
				guess = str(input("Enter guess:\n")).strip()
				print()

		guesses.append(Get_value(guess, correct_word))
		Display_guesses(guesses)
		if Is_correct(guess, correct_word):
			correct = True
			break
	
	print(f"The word was: {correct_word}")
	return Play_again(correct)

def Close() -> None:
	print("Thank you for playing!")

	Write_previous_words()

def Get_previous_words() -> None:
	with open("guessed_words.txt", 'r') as previous:
		for word in previous:
			previous_words.append(word.strip())

def Get_word() -> str:
	f = open(f"../Word_files/5_words.txt", 'r')
	lines = f.readlines()
	f.close()
	l = len(lines)

	not_gotten = True
	while not_gotten:
		word = lines[random.randint(0, l-1)].strip()
		if word not in previous_words:
			not_gotten = False
	
	return word

def Update_previous_words(word: str) -> None:
	previous_words.append(word)
	if len(previous_words) > 20:
		previous_words.pop(0)

def Get_value(guess: str, correct_word: str) -> tuple:
	value = ""
	for i, letter in enumerate(guess):
		current = 0

		if letter in correct_word:
			current = 1
			if correct_word[i] == letter: 
				current = 2

		value += str(current)
	
	return (guess, value)

def Is_correct(guess: str, answer: str) -> bool:
	return guess == answer

def Play_again(correct: bool) -> bool:
	if correct:
		print("Congratulations, you guessed the word correctly!")
	else:
		print("Better luck next time!")
	
	print("Would you like to play again?")
	answer = str(input("Enter y or n:\n")).strip()
	print()

	if answer == 'y':
		return True
	else:
		return False

def Display_guesses(previous_guesses: list) -> None:
	for pair in previous_guesses:
		print(pair[0])
		print(pair[1])
		print()

def Write_previous_words() -> None:
	with open("guessed_words.txt", 'w') as previous:
		for word in previous_words:
			previous.write(f"{word}\n")

if __name__ == '__main__':
	os.chdir(f"{os.getcwd()}/Text_Based")
	Main()