from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")




# TODO: create a snake body
def snake_body(snake_len):
    for turtle_index in range(snake_len):
        new_turtle = Turtle(shape = "square")
        new_turtle.color("white")
        new_turtle.pensize(10)
        # new_turtle.resizemode("user")
        # new_turtle.shapesize(stretch_wid = 10, stretch_len = 10)
        new_turtle.teleport(x = 0 - turtle_index * 20, y = 0)
        new_turtle.penup



# TODO: move the snake


# TODO: control the snake




# TODO: detect collision with food


# TODO: create a scoreboard


# TODO: detect collision with wall


# TODO: detect collision with tail

snake_body(3)

screen.exitonclick()