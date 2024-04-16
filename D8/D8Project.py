import sys
sys.path.append(r'C:\Users\MekChou\OneDrive\Code\Udemy\100-Days-of-Code-Python\module')
from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# combine encrypt and decrypt into caesar
def caesar(plainText, shiftAmount, directionMode):
  cipherText = ""
  # loop to encode each letter in plainText
  if direction == "decode":
    shiftAmount *= -1
  for letter in plainText:
    if letter in alphabet:
      plainIndex = alphabet.index(letter)
      if (plainIndex + shiftAmount) > (len(alphabet) - 1):
        cipherIndex = (plainIndex + shiftAmount) % 26
      elif (plainIndex + shiftAmount) < 0:
        cipherIndex = (plainIndex + shiftAmount) % 26
      else:
        cipherIndex = plainIndex + shiftAmount
      cipherText += alphabet[cipherIndex]
    else:
      cipherText += letter
  print(f"Here's the {directionMode} result: {cipherText}")



print(logo)

goAgain = True

while goAgain:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  if direction in ["encode", "decode"]:
    caesar(text, shift, direction)
  else:
    print("invalid mode")
  result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
  if result == "no":
    goAgain = False
    print("Goodbye")