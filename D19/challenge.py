from turtle import Turtle, Screen


cursor = Turtle()
screen = Screen()

screen.listen()

def move_forwards():
    cursor.forward(10)

def move_backwards():
    cursor.backward(10)

def counter_clockwise():
    cursor.left(5)

def clockwise():
    cursor.right(5)

def clear_drawing():
    cursor.reset()

def key_functions():
    screen.onkeypress(key = "w", fun = move_forwards)
    screen.onkeypress(key = "s", fun = move_backwards)
    screen.onkeypress(key = "a", fun = counter_clockwise)
    screen.onkeypress(key = "d", fun = clockwise)
    screen.onkeypress(key = "c", fun = clear_drawing)
    
    
key_functions()

screen.exitonclick()