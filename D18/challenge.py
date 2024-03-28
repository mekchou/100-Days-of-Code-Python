from turtle import Turtle, Screen
import random

def random_color_hex():
    color = ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    return '#' + color

tim = Turtle()
tim.shape("classic")
tim.pensize(1)
tim.speed(0)
# def draw_shape(num_sides):
    # angle = 360 / num_sides
    # for _ in range(num_sides):
        # tim.forward(100)
        # tim.right(angle)
circles = int(input("Input # of circles you want: "))
angle = int(input("Input the angle you want to turn each time: "))
size = int(input("Input the size of circle: "))
for _ in range (circles):
    tim.pencolor(random_color_hex())
    tim.circle(size)
    tim.left(angle)
    # tim.steps(10)
# sides = int(input("Input # of sides you want to print up to: "))
    
# for _ in range(100):
    # tim.pencolor(random_color_hex())
    # steps = 10
    # angle = random.randint(1,4) * 90
    # tim.right(angle)
    # tim.forward(steps)

input("Press Enter to exit...")