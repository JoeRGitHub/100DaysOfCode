from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

# Password with X length
# The password will be created from s1 to s4 list
# All characters will be random from all lists - Uppercase, Lowercase, Numbers Symbols

s1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']
s2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']
s4 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '/', ']', '[', '{', '}', "'", ':', ',', '.', '/',
      '<', '>', '~', '`', '/']

password = []

def create_random_pass():

    result = s1 + s2 + s3 + s4
    # while len(password) < 6:
    #     password.append(random.choice(result))
    #     #res = [''.join(ele) for ele in password]
    password = random.choices(result, k=10) # With 'choices' no need the loop
    #password.clear()
    one_str = ''.join(password) # Generate the password as a single string
    pass_entry.delete(0, 'end') # Clear the previous password in the entry
    pass_entry.insert(0, one_str) # Insert the newly generated password
    pass_entry.clipboard_clear()
    pass_entry.clipboard_append(one_str) # Copy the string to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    print(use_email_entry.get())
    print(website_entry.get())
    print(pass_entry.get())
    # Save data to file.text
    f = open("db.txt", "a")
    f.write(f'\n{website_entry.get()} | {use_email_entry.get()} | {pass_entry.get()}')
    f.close()
    # Use_email_entry.delete(0, 'end')
    website_entry.delete(0, 'end')
    pass_entry.delete(0, 'end')


    popup()

def popup():
    global top
    top = Toplevel(windows)
    top.geometry("350x100")
    top.title("Approved Window")
    Label(top, text="Info Saved!", font=('Ariel', 16, 'bold')).place(x=132, y=15)
    Button(top, text="Close", font=('Poppins bold', 16), command=close_win).place(x=140, y=55)
    top.transient(windows)  # set to be on top of the main window
    top.grab_set()  # hijack all commands from the master (clicks on the main window are ignored)
    windows.wait_window(top)  # pause anything on the main window until this one closes

def close_win():
    top.destroy()

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=30, pady=30)

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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
## Add cursor to entry
website_entry.focus()
website_entry.insert(END, "")
use_email_entry = Entry(width=35)
use_email_entry.grid(row=2, column=1, columnspan=2)
use_email_entry.insert(END, "default_email@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)
pass_entry.insert(END, "")

# Button's
generate_button = Button(text="Generate Pass", command=create_random_pass)
generate_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)



windows.mainloop()