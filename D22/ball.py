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
        # self.speed(5)
        self.goto(STARTING_POSITIONS)
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.movespeed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.setheading(STARTING_HEADING)
        # self.forward(MOVE_DISTANCE)
        
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.movespeed *= 0.8
    
    def reset_position(self):
        self.goto(STARTING_POSITIONS)
        self.bounce_x()
        self.movespeed *= 0.1