from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.current_score = 0
        # self.shape("blank")
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0, 280)
        self.print_score()

        
    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.print_score()
    
    def print_score(self):
        self.write(f"Score: {self.current_score}", font = ("Arial", 14, "normal"), align = "center")