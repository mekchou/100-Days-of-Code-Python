from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 6, "normal")


class Answer():
    def __init__(self) -> None:
        self.all_answers = []
    
    def print_answer(self, state, x, y):
        new_answer = Turtle()
        new_answer.hideturtle()
        new_answer.penup()
        new_answer.speed(0)
        new_answer.goto(x ,y)
        new_answer.write(state, font=FONT, align= ALIGNMENT)
        self.all_answers.append(new_answer)

    
    
    