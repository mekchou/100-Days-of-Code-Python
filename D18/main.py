import colorgram as cg
import turtle as t
import random as rand

# def rbg_list(color_obj):
#     rgb = []
    
#     for color in color_obj:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         new_color = (r, g, b)
#         rgb.append(new_color)    
#     return rgb

# colors = cg.extract(r"V:\100-Days-of-Code-Python\data\HirstSpot.jpg",40)
# color_list = rbg_list(colors)

# print(colors)
# print(color_list)

color_list = [(198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34), (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59), (193, 190, 192), (17, 78, 98), (215, 184, 172), (190, 190, 195), (78, 72, 31), (156, 108, 114), (38, 66, 91), (167, 200, 209), (108, 130, 150)]


def print_dot(tur, dot_color):
    tur.dot(20, dot_color)
    
def move_right(tur, cur_position):
    tur.setx(cur_position[0] + 50)

def move_nextrow(tur, cur_position):
    tur.setx(cur_position[0] - 50 * 10)
    tur.sety(cur_position[1] + 50)


def main():
    tur = t.Turtle()
    t.colormode(255)
    tur.speed(10)
    tur.hideturtle()
    tur.penup()
    tur.setposition((-250, -250))

    for _ in range(10):
        for _ in range(10):
            print_dot(tur, rand.choice(color_list))
            move_right(tur, tur.position())
        move_nextrow(tur, tur.position())

main()

input("Press Enter to exit...")