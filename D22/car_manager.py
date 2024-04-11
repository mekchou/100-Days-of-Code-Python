from turtle import Turtle
import random as rand

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, y, level):
        super().__init__()
        self.color(rand.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid = 1, stretch_len = 2)
        self.y = y
        self.level = level
        self.goto((300, self.y))
    
    def move(self):
        new_x = self.xcor() - (STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (self.level - 1))
        self.goto((new_x, self.y))