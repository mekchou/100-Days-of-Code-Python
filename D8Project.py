alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

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
        cipherIndex = plainIndex + shiftAmount - 26
      elif (plainIndex + shiftAmount) < 0:
        cipherIndex = plainIndex + shiftAmount + 26
      else:
        cipherIndex = plainIndex + shiftAmount
      cipherText += alphabet[cipherIndex]
    else:
      cipherText += letter
  print(f"Here's the {directionMode} result: {cipherText}")


if direction in ["encode", "decode"]:
  caesar(text, shift, direction)
else:
  print("invalid mode")