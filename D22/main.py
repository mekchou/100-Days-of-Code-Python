import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(key = "Up", fun = player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()



# TODO: build player class with move ability
# TODO: build car class with random color and moving ability
# TODO: create random car and move to left
# TODO: build scoreboard
# TODO: reset player when reaching finish line
# TODO: car speed up when reaching finish line
# TODO: scoreboard +1 when reaching finish line


screen.exitonclick()