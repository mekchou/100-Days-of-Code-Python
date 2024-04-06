from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
# from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 1200, height = 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()


paddle1 = Paddle(-500)
paddle2 = Paddle(500)
screen.onkeypress(key = "w", fun = paddle1.up)
screen.onkeypress(key = "s", fun = paddle1.down)
screen.onkeypress(key = "Up", fun = paddle2.up)
screen.onkeypress(key = "Down", fun = paddle2.down)

ball = Ball()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

# TODO: set up main screen

# TODO: create paddle class that responds to key press

# TODO: create 2 paddles


# TODO: create ball class including ball move

# TODO: add ball bouncing logic

# TODO: detect ball collisions with paddle

# TODO: detect ball goes out of bound

# TODO: create scoreboard class


screen.exitonclick()