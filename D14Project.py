import random
import sys
sys.path.append(r'V:\100-Days-of-Code-Python\module')
sys.path.append(r'V:\100-Days-of-Code-Python\data')
from higher_lower_art import logo, vs
from higher_lower_game_data import data


# format data
def formatData(account):
    accountName = account["name"]
    # accountfollowerCount = account["follower_count"]
    accountDescription = account["description"]
    accountCountry = account["country"]
    return f"{accountName}, a {accountDescription}, from {accountCountry}"


# check answer
def check(a, b, answer, currentScore):
    if answer == "A" and a["follower_count"] > b["follower_count"]:
        return True
    elif answer == "B" and a["follower_count"] < b["follower_count"]:
        return True
    else:
        return False

# randompick
def randomPick():
    return random.choice(data)


def game():
    score = 0
    continueGame = True
    accountA = randomPick()
    accountB = randomPick()

    while continueGame:
        # print logo
        print(logo)
        # Generate a random account from the game data
        if score > 0:
            print(f"You're right! Current score: {score}.")
        print("Compare A: " + formatData(accountA))

        # print vs
        print(vs)

        print("Against B: " + formatData(accountB))
        # ask answer
        answer = input("Who has more followers? Type 'A' or 'B': ")
        # if correct, add score and prepare next round
        if check(accountA, accountB, answer, score):
            score += 1
            if answer == "B":
                accountA = accountB
            accountB = randomPick()
        else:
            break
# print when game ends
    print(f"Sorry, that's wrong. Final score: {score}")

game()