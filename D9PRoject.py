import sys
sys.path.append(r'C:\Users\MekChou\OneDrive\Code\Udemy\100-Days-of-Code-Python\module')
from auction_art import logo
# create empty dict that stores input
bidData = {}

# create function that takes input and write to dict
def bidInput(name, bid):
  bidData[name] = bid

# create function that return the highest bidder from dict
def highestBid(bidDataDict):
  # maxBid = max(bidDataDict.values())
  maxKey = max(bidDataDict, key = bidDataDict.get)
  maxValue = bidDataDict[maxKey]
  return (maxKey, maxValue)

# create function that asks for input
def question():
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  return (name, bid)


# main section

otherBid = True
print(logo)
# loop over question when other bid
while otherBid:
  name, bid = question()
  bidInput(name, bid)
  nextBid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if nextBid == 'no':
    otherBid = False
  elif nextBid == 'yes':
    otherBid = True
# calculate max and print result
maxKey, maxValue = highestBid(bidData)
print(f"The winner is {maxKey} with a bid of ${maxValue}.")
