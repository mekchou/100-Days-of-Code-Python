from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 28, "normal")


class Scoreboard(Turtle):
    
    def __init__(self, x):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(x, 350)
        self.print_score()

        
    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.print_score()
    
    def print_score(self):
        self.write(self.current_score, font = FONT, align = ALIGNMENT)
    
    # def game_over(self):
        # self.goto(0, 0)
        # self.write("Game Over!", font = FONT, align = ALIGNMENT)