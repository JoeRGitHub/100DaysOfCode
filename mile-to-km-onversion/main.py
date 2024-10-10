
from tkinter import *

window =Tk()
window.title("Mile to Km Converter")
window.minsize(width=210, height=200)
# Frame around the window
window.config(padx=50, pady=50)

def butten_click():
    km = float(miles_text_filed.get()) * 1.609
    result_filed["text"] = round(km, 2)

miles_text_filed = Entry(width=10)
miles_text_filed.insert(END, string="0")
miles_text_filed.grid(row=0, column=2)

miles_label = Label(text="Miles", font=("Arial", 15))
miles_label.grid(row=0, column=3)

is_equal_label = Label(text="Is equal to:", font=("Arial", 15))
is_equal_label.grid(row=1, column=1)

# Text square
km_text_field = Entry(width=10, )
km_text_field.insert(END, string="")
km_text_field.grid(row=1, column=2)

# Black box
black_box = Text(height=1.5, width=13)
black_box.insert(END, "")
black_box.grid(row=1, column=2)

result_filed = Label(text="0", font=("Arial", 14))
result_filed.grid(row=1, column=2)

km_label = Label(text="Km", font=("Arial", 15))
km_label.grid(row=1, column=3)

calc_button = Button(text="Convert Miles to Km", command=butten_click)
calc_button.grid(row=2 , column=2)


window.mainloop()