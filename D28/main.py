import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomoto_img = tkinter.PhotoImage(file=r"data\tomato.png")
canvas.create_image(100, 112, image=tomoto_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start")
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset")
reset_button.grid(column=2, row=2)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

check_label = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
