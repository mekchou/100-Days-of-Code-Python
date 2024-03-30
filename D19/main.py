from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): ")




def initialize():
    for turtle_index in range(6):
        new_turtle = Turtle(shape = "turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x = -230, y = y_positions[turtle_index])
        all_turtles.append(new_turtle)


def move_forwards(turtle):
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)

# screen.listen()
# screen.onkey(key = "space", fun = move_forwards)
def main():
    is_race_on = False
    if user_bet in colors:
        is_race_on = True
        initialize()
    else:
        print("Invalid color")
        
    while is_race_on:
        for turtle in all_turtles:
            move_forwards(turtle)
            if turtle.xcor() >= 240:
                winner = turtle
                print(f"{colors[all_turtles.index(winner)]} turtle is the winner!")
                if user_bet == colors[all_turtles.index(winner)]:
                    print("Your guess was correct!")
                else: 
                    print("Your guess was incorrect!")
                is_race_on = False
                break

main()

screen.exitonclick()