from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
# TODO: create a snake body
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # TODO: move the snake
    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1): 
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)


    # TODO: control the snake
    def up(self):
        if self.head.heading() != UP and  self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP and  self.head.heading() != DOWN:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != LEFT and  self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT and  self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        new_segment = Turtle(shape = "square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)
        
    def extend(self):
        self.add_segment(self.snake[-1].position())
        
    def reset(self):
        for segment in self.snake:
            segment.goto(2000,2000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]