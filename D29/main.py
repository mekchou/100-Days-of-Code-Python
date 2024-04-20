import tkinter as tk
from tkinter import messagebox
import string as string
import random as rand
import pyperclip
import json

FONT_NAME = "Courier"
FONT_SIZE = 8




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, "end")
    symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']
    nr_letters = rand.randint(8,10)
    nr_numbers = rand.randint(2,4)
    nr_symbols = rand.randint(2,4)

    pwList = []

    pw_letters = [rand.choice(string.ascii_letters) for _ in range(nr_letters)]
    pw_symbols = [rand.choice(symbol) for _ in range(nr_symbols)]
    pw_numbers = [str(rand.randint(0,9)) for _ in range(nr_numbers)]
    pwList = pw_letters + pw_symbols + pw_symbols

    rand.shuffle(pwList)
    pw = "".join(pwList)

    password_entry.insert(tk.END, pw)
    pyperclip.copy(pw)

# print(f"Your password is: {pw}")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    
    
    # notification for empty field
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
    
    # popup for confirmation
        proceed = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: {username}\nPassword: {password} \nIs it ok to save?")
        if proceed:
            try:
                with open("D29\passwords.json", mode = "r") as data_file:
                # read old data
                    data = json.load(data_file)
                # updating old data with new one
                    data.update(new_data)
            except FileNotFoundError:
                with open("D29\passwords.json", mode = "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("D29\passwords.json", mode = "w") as data_file:
                    # saving updated data
                    json.dump(data, data_file, indent=4)
                
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


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
website_entry.focus()

username_entry = tk.Entry(width=52)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
username_entry.insert(tk.END, "mek.chou@gmail.com")

password_entry = tk.Entry(width=31)
password_entry.grid(column=1, row=3, sticky="w")

generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w")

add_button = tk.Button(text="Add", width=44, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")






window.mainloop()