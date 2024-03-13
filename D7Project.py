import random
import string

wordList = ["cat", "rainbow", "dragonball"]
chosenWord = random.choice(wordList) 
guess = ""
display = []
endOfGame = False
for letter in chosenWord:
  display.append("_")

while not endOfGame:
  while not (len(guess) == 1 and guess in string.ascii_letters):
    guess = input("guess a letter\n").lower()
  for num in range(len(chosenWord)):
    if chosenWord[num] == guess:
      # print("Right")
      display[num] = guess
    # else:
      # print("Wrong")
  print(display)
  if "_" not in display:
    endOfGame = True
    print("you win!")
  else:
    guess = ""

print(f"the word is {chosenWord}")
# print(f"letter entered is {guess}")
