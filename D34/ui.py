import tkinter as tk
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuestionGui:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.score = 0
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(
            text=f"Score: {self.score}", bg=THEME_COLOR, fg="white"
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(
            150, 125, font=FONT, text="Question", width=280
        )

        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0, pady=20)

        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
