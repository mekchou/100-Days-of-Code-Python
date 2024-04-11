import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key = "Up", fun = player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move(scoreboard.level)

# detect car going into finish line
    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        scoreboard.next_level()

# detect collision with car
    for car in car_manager.all_cars:
        hit_distance = 30
        if player.ycor() >= car.ycor() - 20 and player.distance(car) < hit_distance:
            scoreboard.game_over()
            game_is_on = False


# TODO: build player class with move ability
# TODO: build car class with random color and moving ability
# TODO: create random car and move to left
# TODO: build scoreboard
# TODO: crete gameover in scoreboard
# TODO: reset player when reaching finish line
# TODO: car speed up when reaching finish line
# TODO: scoreboard +1 when reaching finish line
# TODO: detect collission with car


screen.exitonclick()