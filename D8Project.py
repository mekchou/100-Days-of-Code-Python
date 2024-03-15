alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# encrypt
def encrypt(plainText, shiftAmount):
  cipherText = ""
  # loop to encode each letter in plainText
  for letter in plainText:
    if letter in alphabet:
      plainIndex = alphabet.index(letter)
      if (plainIndex + shiftAmount) > (len(alphabet) - 1):
        cipherIndex = plainIndex + shiftAmount - 26
      else:
        cipherIndex = plainIndex + shiftAmount
      cipherText += alphabet[cipherIndex]
    else:
      cipherText += letter
  print(f"Here's the encoded result: {cipherText}")

# decrypt
def decrypt(plainText, shiftAmount):
  cipherText = ""
  # loop to encode each letter in plainText
  for letter in plainText:
    plainIndex = alphabet.index(letter)
    if (plainIndex - shiftAmount) < 0:
      cipherIndex = plainIndex - shiftAmount + 26
    else:
      cipherIndex = plainIndex - shiftAmount
    cipherText += alphabet[cipherIndex]
  print(f"Here's the decoded result: {cipherText}")


if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
else:
  print("invalid mode")