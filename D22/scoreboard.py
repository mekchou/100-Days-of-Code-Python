from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.goto(-210,250)
        self.print_score()
    
    def print_score(self):
        self.write(f"Level: {self.level}", font = FONT, align = ALIGNMENT)
        
    def next_level(self):
        self.level += 1
        self.print_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", font = FONT, align = ALIGNMENT)