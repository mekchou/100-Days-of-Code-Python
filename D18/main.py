from turtle import Turtle, Screen
import random

def random_color_hex():
    color = ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    return '#' + color

tim = Turtle()
tim.shape("classic")
tim.pensize(5)
tim.speed(8)
# def draw_shape(num_sides):
    # angle = 360 / num_sides
    # for _ in range(num_sides):
        # tim.forward(100)
        # tim.right(angle)

    
# sides = int(input("Input # of sides you want to print up to: "))
    
for _ in range(100):
    tim.pencolor(random_color_hex())
    steps = 10
    angle = random.randint(1,4) * 90
    tim.right(angle)
    tim.forward(steps)

input("Press Enter to exit...")