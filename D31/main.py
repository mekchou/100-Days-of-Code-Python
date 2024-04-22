import tkinter as tk
import pandas as pd
import random as rand

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
TITLE_FONT_SIZE = 40
TITLE_FONT_STYLE = "italic"
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
    current_card = rand.choice(data_dict)
    # new_random_word = current_card["French"]
    canvas.itemconfig(card_title, text = "French")
    canvas.itemconfig(card_word, text = current_card["French"])
    # print(new_random_word)

# flip the card



# UI setup
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526)
card_front = tk.PhotoImage(file="images\card_front.png")
canvas.create_image(400,263,image = card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text= "Title", font=(FONT, TITLE_FONT_SIZE, TITLE_FONT_STYLE))
card_word = canvas.create_text(400, 263, text= "Word", font=(FONT, WORD_FONT_SIZE, WORD_FONT_STYLE))



canvas.grid(column=0, row=0, columnspan=2)

# TITLE_label = tk.Label(text = "French", font=(FONT, TITLE_FONT_SIZE, TITLE_FONT_STYLE), bg="white")
# TITLE_label.place(x=400, y=150, anchor="center")

# word_label = tk.Label(text = "Word", font=(FONT, WORD_FONT_SIZE, WORD_FONT_STYLE), bg="white")
# word_label.place(x=400, y=285, anchor="center", )

right_image = tk.PhotoImage(file=r"images\right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=next_word)
right_button.grid(column=1, row=1)

wrong_image = tk.PhotoImage(file=r"images\wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(column=0, row=1)


window.mainloop()