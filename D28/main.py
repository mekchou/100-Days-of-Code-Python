import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    # reset timer
    canvas.itemconfig(timer_text, text = "00:00")
    # reset timer_label
    timer_label.config(text="Timer")
    # reset check_marks
    check_label.config(text="")
    # reset reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60    

    reps += 1
    # while reps <= 8:
    if reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)  
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            check_label.config(text=marks)
        
        
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomoto_img = tkinter.PhotoImage(file=r"data\tomato.png")
canvas.create_image(100, 112, image=tomoto_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

check_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
check_label.grid(column=1, row=3)





window.mainloop()
