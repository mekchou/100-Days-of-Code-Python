import random
import string

wordList = ["cat", "rainbow", "dragonball"]
chosenWord = random.choice(wordList) 
guess = ""
display = []
endOfGame = False
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = len(stages)-1

# initialize display word
for letter in chosenWord:
  display.append("_")
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
