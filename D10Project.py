
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

num1 = int(input("What's the fist number?: "))
num2 = int(input("What's the second number?: "))
for symbol in operations:
  print(symbol)
operationSymbol = input("Pick an operation from the line above: ")
answer = operations[operationSymbol](num1, num2)
print(f"{num1} {operationSymbol} {num2} = {answer}")