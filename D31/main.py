import tkinter as tk
import pandas as pd
import random as rand

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
TITLE_FONT_SIZE = 40
TITLE_FONT_STYLE = "italic"
WORD_FONT_SIZE = 60
WORD_FONT_STYLE = "bold"
FRENCH_WORDS = "data/french_words.csv"
WORDS_TO_LEARN = "D31/words_to_learn.csv"
current_card = {}


# create new flash cards
# read csv
# if words_to_learn exist then take it, otherwise read french_words.csv
try:
    dataframe = pd.read_csv(WORDS_TO_LEARN)
except FileNotFoundError:
    dataframe = pd.read_csv(FRENCH_WORDS)

data_dict = dataframe.to_dict(orient="records")


# pick random french word and translation into flashcard

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = rand.choice(data_dict)
    except IndexError:
        print("You Learned all the word!")
        canvas.itemconfig(card_image, image= card_back)
        canvas.itemconfig(card_title, text = "Good Job", fill="white")
        canvas.itemconfig(card_word, text = "No words left!", fill="white")
    else:    
        canvas.itemconfig(card_image, image= card_front)
        canvas.itemconfig(card_title, text = "French", fill="black")
        canvas.itemconfig(card_word, text = current_card["French"], fill="black")
        flip_timer = window.after(3000, func=flip_card)

# flip the card
def flip_card():
    canvas.itemconfig(card_image, image = card_back)
    canvas.itemconfig(card_title, text= "English", fill="white")
    canvas.itemconfig(card_word, text= current_card["English"], fill="white")

# remove word when click right button
def right_word():
    if current_card in data_dict:
        data_dict.remove(current_card)
    save_file()
    next_word()

def wrong_word():
    next_word()

def save_file():
    new_dataframe = pd.DataFrame(data_dict)
    new_dataframe.to_csv(WORDS_TO_LEARN, index = False)



# UI setup
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(30000, func=flip_card)


canvas = tk.Canvas(width=800, height=526)
card_front = tk.PhotoImage(file="images\card_front.png")
card_back = tk.PhotoImage(file="images\card_back.png")
card_image = canvas.create_image(400,263,image = card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text= "Title", font=(FONT, TITLE_FONT_SIZE, TITLE_FONT_STYLE))
card_word = canvas.create_text(400, 263, text= "Word", font=(FONT, WORD_FONT_SIZE, WORD_FONT_STYLE))


canvas.grid(column=0, row=0, columnspan=2)


right_image = tk.PhotoImage(file=r"images\right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=right_word)
right_button.grid(column=1, row=1)

wrong_image = tk.PhotoImage(file=r"images\wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=wrong_word)
wrong_button.grid(column=0, row=1)

# flip_card(0)
window.mainloop()