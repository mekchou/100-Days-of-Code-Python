import random as rand
import string as string

lettersC = int(input("How many letters would you like in your password?\n"))
symbolsC = int(input("How many symbols would you like?\n"))
numbersC = int(input("How many numbers would you like?\n"))

symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']
pwList = []



for count in range(lettersC):
  pwList.append(rand.choice(string.ascii_letters))
for count in range(symbolsC):
  pwList.append(rand.choice(symbol))
for count in range(numbersC):
  pwList.append(str(rand.randint(0,9)))

rand.shuffle(pwList)
pw = "".join(pwList)

print(f"Your password is: {pw}")