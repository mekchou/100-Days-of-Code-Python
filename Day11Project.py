############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

import random
import sys
sys.path.append(r'C:\Users\MekChou\OneDrive\Code\Udemy\100-Days-of-Code-Python\module')
from blackjack_art import logo
# create list of deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# create function to add new card
def newCard():
  return random.choice(cards)

# create function to distribute initial deck
def initialDeck():
  deck = []
  deck.append(random.choice(cards))
  deck.append(random.choice(cards))
  return deck

# function to calculate score
def scoreSum(deck):
  score = 0
  for num in deck:
    score += num
  return score

def welcome():
  print(logo)

# start a game function
def game():
  playGame = input("Do you want to plan a game of Bkackjack? Type 'y' or 'n': ")
  if playGame == "y":

    # initialize game
    playerDeck = initialDeck()
    computerDeck = initialDeck()
    # computerDeck = [11,5]
    # print(playerDeck)
    # print(computerDeck)
    playerScore = scoreSum(playerDeck)
    computerScore = scoreSum(computerDeck)

    addCard = True

    welcome()
    # while loop to continue game
    while addCard:
    # lose if player > 21
      if playerScore > 21:
        # replace 11 with 1
        if 11 in playerDeck:
          aIndex = playerDeck.index(11)
          playerDeck[aIndex] = 1
          playerScore = scoreSum(playerDeck)
        # if no 11 in deck to be replaced
        else:
        # print cards
          print(f"Your final hand: {playerDeck}, final score: {playerScore}")
          print(f"Computer's final hand: {computerDeck}, final score: {computerScore}")
          print("You went over. You lose")
          addCard = False
          break
      print(f"Your cards: {playerDeck}, current score: {playerScore}")
      print(f"Computer's first card: {computerDeck[0]}")
    # ask for new card
      addCardString = input("Type 'y' to get another card, type 'n' to pass: ")

      if addCardString == "y":
        playerDeck.append(newCard())
        playerScore = scoreSum(playerDeck)
      elif addCardString == "n":
        addCard = False
            # add card to computer in score < 17
        while computerScore < 17:
          computerDeck.append(newCard())
          computerScore = scoreSum(computerDeck)
          # check if computer > 21
          while computerScore > 21:
            # replace 11 with 1 if any
            if 11 in computerDeck:
              aIndex = computerDeck.index(11)
              computerDeck[aIndex] = 1
              computerScore = scoreSum(computerDeck)
            # if no 11 in deck to be replaced and > 21
            else:
              print(f"Your final hand: {playerDeck}, final score: {playerScore}")
              print(f"Computer's final hand: {computerDeck}, final score: {computerScore}")
              print("Opponent went over. You win")
              break          

        print(f"Your final hand: {playerDeck}, final score: {playerScore}")
        print(f"Computer's final hand: {computerDeck}, final score: {computerScore}")
          # check computerScore vs player if computer < 21
        if playerScore == computerScore:
          print("Draw")
        elif playerScore > computerScore:
          print("Your win")
        else:
          print("Computer win")
    game()

game()