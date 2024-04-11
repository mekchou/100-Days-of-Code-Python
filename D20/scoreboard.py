from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.current_score = 0
        # self.shape("blank")
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0, 280)
        self.print_score()

        
    def increase_score(self):
        self.current_score += 1
        self.print_score()
    
    def print_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", font = FONT, align = ALIGNMENT)
 
    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.print_score()
        
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", font = FONT, align = ALIGNMENT)