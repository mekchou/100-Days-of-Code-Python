import tkinter

FONT = ("Arial", 10)


# set up window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)


# button action
def convert():
    miles_number = round(float(miles_value.get()), 2)
    km_value.config(text=round(miles_number * 1.609, 2))


# create objects
miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km_value = tkinter.Label(text=0)
km_value.grid(column=1, row=1)

miles_value = tkinter.Entry(width=10)
miles_value.insert(tkinter.END, string=0)
miles_value.grid(column=1, row=0)

calculate = tkinter.Button(width=10, text="Calculate", command=convert)
calculate.grid(column=1, row=2)


window.mainloop() 
