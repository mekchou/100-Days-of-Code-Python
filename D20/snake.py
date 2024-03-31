from turtle import Screen, Turtle



class Snake:
# TODO: create a snake body
    def __init__(self):
        starting_positions = []
        snake = []
        for turtle_index in range(3):
            new_segment = Turtle(shape = "square")
            new_segment.color("white")
            new_segment.penup()
            starting_positions.append((0 - turtle_index * 20, 0))
            new_segment.goto(starting_positions[turtle_index])
        snake.append(new_segment)

    # TODO: move the snake
    def move_snake(snake):
        for seg_num in range(len(snake) - 1, 0, -1): 
            new_x = snake[seg_num - 1].xcor()
            new_y = snake[seg_num - 1].ycor()
            snake[seg_num].goto(new_x, new_y)

        snake[0].left(90)
        snake[0].forward(20)


    # TODO: control the snake




    # TODO: detect collision with food


    # TODO: create a scoreboard


    # TODO: detect collision with wall


    # TODO: detect collision with tail
