from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(key = "Up", fun = snake.up)
screen.onkeypress(key = "Down", fun = snake.down)
screen.onkeypress(key = "Left", fun = snake.left)
screen.onkeypress(key = "Right", fun = snake.right)





game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()