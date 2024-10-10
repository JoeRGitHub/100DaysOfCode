from tkinter import *
from PIL import ImageTk, Image
import os




# Label | Entry | Button
# tk columnspan
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid (row=0,column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
use_email_label = Label(text="Email/Username:")
use_email_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=31)
website_entry.grid(row=1, column=1)
use_email_entry = Entry(width=21)
use_email_entry.grid(row=2, column=1)
pass_entry = Entry(width=36)
pass_entry.grid(row=3, column=1)

# Button's
website_button = Button(text="Generate Password")
website_button.grid(row=3, column=4)
add_button = Button(text="Add")
add_button.grid(row=4, column=1)



windows.mainloop()