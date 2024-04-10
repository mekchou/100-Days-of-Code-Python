from turtle import Screen, Turtle   
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = Screen()
screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
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

scoreboard1 = Scoreboard(-100)
scoreboard2 = Scoreboard(100)

game_is_on = True

initialspeed = 0.1
speedfactor = initialspeed

while game_is_on:
    time.sleep(speedfactor)
    screen.update()
    ball.move()

# detect collision with wall
    if ball.ycor() > (SCREEN_HEIGHT/2 - 20) or ball.ycor() < (-SCREEN_HEIGHT/2 + 20):
        ball.bounce_y()

# detect collision with paddle
    if ball.xcor() > (paddle2.xcor() - 30) and ball.distance(paddle2) < 50:
        ball.bounce_x()
        speedfactor *= 0.8
    elif ball.xcor() < (paddle1.xcor() + 30) and ball.distance(paddle1) < 50:
        ball.bounce_x()
        speedfactor *= 0.8

    
# detect if ball out of bound
    if ball.xcor() > SCREEN_WIDTH/2:
        ball.reset_position()
        scoreboard1.increase_score()
        speedfactor = initialspeed
    elif ball.xcor() < -SCREEN_WIDTH/2:
        ball.reset_position()
        scoreboard2.increase_score()
        speedfactor = initialspeed

# TODO: set up main screen

# TODO: create paddle class that responds to key press

# TODO: create 2 paddles


# TODO: create ball class including ball move

# TODO: add ball bouncing logic

# TODO: detect ball collisions with paddle

# TODO: detect ball goes out of bound

# TODO: create scoreboard class


screen.exitonclick()