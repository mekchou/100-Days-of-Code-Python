from turtle import Turtle, Screen
import random

def random_color_hex():
    color = ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    return '#' + color

tim = Turtle()
tim.shape("classic")

def draw_shape(num_sides):
    angle = 360 / num_sides
    tim.pencolor(random_color_hex())
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
    
    
sides = int(input("Input # of sides you want to print up to: "))
    
for shape in range(3, sides + 1):
    draw_shape(shape)

input("Press Enter to exit...")