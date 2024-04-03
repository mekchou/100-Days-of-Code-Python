from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

# detect collision with food
    if snake.head.distance(food) <= 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
# detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) <= 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()