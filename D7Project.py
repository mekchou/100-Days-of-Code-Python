import random
import string

wordList = ["cat", "rainbow", "dragonball"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosenWord = random.choice(wordList) 

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = ""
while not (len(guess) == 1 and guess in string.ascii_letters):
  guess = input("guess a letter\n").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in range(chosenWord):
  if letter == guess:
    print("Right")
  else:
    print("Wrong")
print(f"the word is {chosenWord}")
print(f"letter entered is {guess}")