import random

def answer():
    return random.randint(1, 100)

# function to choose difficulty
def difficultyAttempts(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5


# function to decide result
def showResult(num, answerNum, attempts):
    # global attempts
    if num == answerNum:
        print(f"You got it! The answer was {answerNum}")
        return -1
    elif num > answerNum:
        print("Too high.")
        print("Guess again.")
        attempts -= 1
    else:
        print("Too low.")
        print("Guess again.")
        attempts -= 1
    return attempts


def game():
    print("Welcome to the NUmber Guessing Game!")
    print("I'm thinking of a numebr between 1 and 100.")
    answerNum = answer()

    difficultyLv = input("Type 'easy' or 'hard': ")
    attempts = difficultyAttempts(difficultyLv)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessNum = int(input("Make a guess: "))
        attempts = showResult(guessNum, answerNum, attempts)
        if  attempts == -1:
            break
        elif attempts == 0:
            print("You've run out of guesses, you lose.")
            
game()