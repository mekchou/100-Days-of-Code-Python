alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plainText, shiftAmount):
  cipherText = ""
  # loop to encode each letter in plainText
  for letter in plainText:
    plainIndex = alphabet.index(letter)
    if (plainIndex + shiftAmount) > (len(alphabet) - 1):
      cipherIndex = plainIndex + shiftAmount - 26
    else:
      cipherIndex = plainIndex + shiftAmount
    cipherText += alphabet[cipherIndex]
  print(f"Here's the encoded result: {cipherText}")


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction == "encode":
  encrypt(text, shift)