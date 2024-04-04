from turtle import Turtle
STARTING_POSITIONS = [-30, -10, 10, 30]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
# LEFT = 180
# RIGHT = 0


class Paddle(Turtle):
    def __init__(self, x):
        self.paddle = []
        self.x = x
        self.create_paddle()
                
    def create_paddle(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape = "square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto((self.x, position))
            self.paddle.append(new_segment)

    def up(self):
        for segment in range(len(self.paddle)):
            new_y = self.paddle[segment].ycor() + MOVE_DISTANCE
            self.paddle[segment].goto((self.x, new_y))         
        
    def down(self):
        for segment in range(len(self.paddle)):
            new_y = self.paddle[segment].ycor() - MOVE_DISTANCE
            self.paddle[segment].goto((self.x, new_y))
