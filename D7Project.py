import random
import string
import sys
sys.path.append(r'C:\Users\MekChou\OneDrive\Code\Udemy\100-Days-of-Code-Python\module')
from hangman_art import logo
from hangman_art import stages
import hangman_words

chosenWord = random.choice(hangman_words.word_list) 
guess = ""
display = []
endOfGame = False

lives = len(stages)-1

# initialize display word
for letter in chosenWord:
  display.append("_")
# start of game
print(logo)
# if endOfGane = false
while not endOfGame:
  # re enter in input is invalid
  while not (len(guess) == 1 and guess in string.ascii_letters):
    guess = input("guess a letter\n").lower()
  
  # update display word
  for num in range(len(chosenWord)):
    if chosenWord[num] == guess:
      display[num] = guess
  
  # lives -1 if guess incorrect
  if guess not in chosenWord:
    lives -= 1
    print(f"{guess} is not in the word")
  # let user know if letter is guessed
  if guess in display:
    print(f"{guess} has already been guessed")
  
  # print display word
  print(display)
  # print stages
  print(stages[lives])
  # end game if lives = 0
  if lives == 0:
    endOfGame = True
    print("you lose!")
  
  # check if game is finished
  elif "_" not in display:
    endOfGame = True
    print("you win!")
  else:
    guess = ""

# output chosenWord for validation
print(f"the word is {chosenWord}")
# print(f"letter entered is {guess}")
