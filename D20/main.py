from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")


snake = []
game_is_on = True

# TODO: create a snake body
def snake_body(snake_len):
    starting_positions = []
    for turtle_index in range(snake_len):
        new_segment = Turtle(shape = "square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed(0)
        # new_segment.pensize(10)
        starting_positions.append((0 - turtle_index * 20, 0))
        # print(starting_positions[turtle_index])
        # new_segment.teleport(starting_positions[turtle_index])
        new_segment.goto(starting_positions[turtle_index])
        snake.append(new_segment)



# TODO: move the snake
def move_snake(snake):
    while game_is_on:
        for seg in snake:
            seg.forward(20)


# TODO: control the snake




# TODO: detect collision with food


# TODO: create a scoreboard


# TODO: detect collision with wall


# TODO: detect collision with tail

snake_body(3)
move_snake(snake)

screen.exitonclick()