import tkinter as tk
FONT_NAME = "Courier"
FONT_SIZE = 8




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# convas
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file=r"data\passwordlogo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column=1,row=0)


# objects
website_label = tk.Label(text="Website:", font=(FONT_NAME, FONT_SIZE))
website_label.grid(column=0, row=1)

username_label = tk.Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
username_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
password_label.grid(column=0, row=3)

website_entry = tk.Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")

username_entry = tk.Entry(width=52)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")

password_entry = tk.Entry(width=31)
password_entry.grid(column=1, row=3, sticky="w")

generate_password_button = tk.Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="w")

add_button = tk.Button(text="Add", width=44)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")






window.mainloop()