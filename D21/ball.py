from turtle import Turtle
STARTING_POSITIONS = (0, 0)
MOVE_DISTANCE = 10
STARTING_HEADING = 45

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(1)
        self.goto(STARTING_POSITIONS)

    def move(self):
        new_x = self.xcor() + MOVE_DISTANCE
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x, new_y)
        # self.setheading(STARTING_HEADING)
        # self.forward(MOVE_DISTANCE)
        
