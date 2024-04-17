import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx = 50, pady = 50)

# label
my_label = tkinter.Label(text="Label", font=("Arial", 12, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)


# button
def button_clicked():
    print("I got clicked")
    # my_label["text"] = "Button got clicked"
    # my_label.config(text = "Button got clicked")
    my_label.config(text = input.get())

button = tkinter.Button(text = "Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row = 1)

button2 = tkinter.Button(text = "Click Me!!!")
button2.grid(column=2, row = 0)

# entry
input = tkinter.Entry(width = 10)
# input.pack()
input.grid(column=3, row=2)
# my_label.config(text = input.get())






window.mainloop()




# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     print(total)
    
    
# add(1,2,3)