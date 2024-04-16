import sys
sys.path.append(r'C:\Users\MekChou\OneDrive\Code\Udemy\100-Days-of-Code-Python\module')
from calc_art import logo
# plus function
def add(m, n):
  return m + n
# minus function
def substract(m, n):
  return m - n

# multiple function
def multiply(m, n):
  return m * n

# divide function
def divide(m, n):
  return m / n

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

# function = operations["+"]
# print(function(2,3))


def calculator():
  print(logo)

  continueCalc = True
  num1 = float(input("What's the fist number?: "))
  for symbol in operations:
    print(symbol)

  while continueCalc:
    operationSymbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    answer = operations[operationSymbol](num1, num2)
    print(f"{num1} {operationSymbol} {num2} = {answer}")

    continueCheck = input(f"Type 'y' to continue calculating witn {answer}, or type 'n' to start a new calculation, or type others to exit: ")
    if continueCheck == "y":
      num1 = answer
    elif continueCheck == "n":
      continueCalc = False
      calculator()
    else:
      break

calculator()