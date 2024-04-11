from turtle import Turtle
import random as rand

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        
    def create_car(self):
        random_chance = rand.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            new_car.color(rand.choice(COLORS))
            new_car.penup()
            random_y = rand.randint(-250, 250)
            new_car.goto((300, random_y))
            self.all_cars.append(new_car)
    
    def move(self, level):
        for car in self.all_cars:
            # new_x = car.xcor() - (STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1))
            # self.goto((new_x, car.ycor()))
            car.backward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1))