from turtle import Turtle
STARTING_POSITIONS = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
# LEFT = 180
# RIGHT = 0


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.x = x
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.goto((self.x, STARTING_POSITIONS))
                
    # def create_paddle(self):
    #     new_segment = Turtle(shape = "square")
    #     new_segment.color("white")
    #     new_segment.penup()
    #     new_segment.goto((self.x, STARTING_POSITIONS))
    #     self.paddle.append(new_segment)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto((self.x, new_y))         
        
    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto((self.x, new_y))       