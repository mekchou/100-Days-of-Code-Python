import random
import string

wordList = ["cat", "rainbow", "dragonball"]
chosenWord = random.choice(wordList) 
guess = ""
display = []

for letter in chosenWord:
  display.append("_")

while not (len(guess) == 1 and guess in string.ascii_letters):
  guess = input("guess a letter\n").lower()



for num in range(len(chosenWord)):
  if chosenWord[num] == guess:
    print("Right")
    display[num] = guess
  else:
    print("Wrong")


print(f"display is \n {display}")
print(f"the word is {chosenWord}")
print(f"letter entered is {guess}")