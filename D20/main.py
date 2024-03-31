from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = []
game_is_on = True

# TODO: create a snake body
def snake_body(snake_len):
    starting_positions = []
    for turtle_index in range(snake_len):
        new_segment = Turtle(shape = "square")
        new_segment.color("white")
        new_segment.penup()
        # new_segment.speed(5)
        # new_segment.pensize(10)
        starting_positions.append((0 - turtle_index * 20, 0))
        # print(starting_positions[turtle_index])
        # new_segment.teleport(starting_positions[turtle_index])
        new_segment.goto(starting_positions[turtle_index])
        snake.append(new_segment)



# TODO: move the snake
def move_snake(snake):
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(snake) - 1, 0, -1): 
            new_x = snake[seg_num - 1].xcor()
            new_y = snake[seg_num - 1].ycor()
            snake[seg_num].goto(new_x, new_y)
        snake[0].forward(20)


# TODO: control the snake




# TODO: detect collision with food


# TODO: create a scoreboard


# TODO: detect collision with wall


# TODO: detect collision with tail

snake_body(3)
screen.update()
move_snake(snake)

screen.exitonclick()