from turtle import Turtle, Screen


tim = Turtle()

tim.shape("turtle")
tim.color("red")
for num in range(50):
    tim.forward(10)
    if num % 2 == 0:
        tim.up()
    else:
        tim.down()

input("Press Enter to exit...")