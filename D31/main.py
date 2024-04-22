import tkinter as tk
import pandas as pd
import random as rand

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
LANGUAGE_FONT_SIZE = 40
LANGUAGE_FONT_STYLE = "italic"
WORD_FONT_SIZE = 60
WORD_FONT_STYLE = "bold"


# create new flash cards
# read csv
dataframe = pd.read_csv(r"data\french_words.csv")
# print(dataframe)
data_dict = dataframe.to_dict(orient="records")
# print(data_dict)


# pick random french word and translation into flashcard

def next_word():
    new_random_word = rand.choice(data_dict)["French"]
    word_label.config(text=new_random_word)
    # print(new_random_word)





# UI setup
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526)
card_front = tk.PhotoImage(file="images\card_front.png")
canvas.create_image(400,263,image = card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

language_label = tk.Label(text = "French", font=(FONT, LANGUAGE_FONT_SIZE, LANGUAGE_FONT_STYLE), bg="white")
language_label.place(x=400, y=150, anchor="center")

word_label = tk.Label(text = "Word", font=(FONT, WORD_FONT_SIZE, WORD_FONT_STYLE), bg="white")
word_label.place(x=400, y=285, anchor="center", )

right_image = tk.PhotoImage(file=r"images\right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=next_word)
right_button.grid(column=1, row=1)

wrong_image = tk.PhotoImage(file=r"images\wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(column=0, row=1)


window.mainloop()