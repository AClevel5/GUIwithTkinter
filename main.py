from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=500)

def button_clicked():
    print("nice")

my_label = Label(window, text="My first GUI Program")
my_label.config(text="New Text")
my_label.grid(row=0, column=0)

button = Button(window, text="Click me", command= button_clicked)
button.grid(row=1, column=1)

input = Entry(width=10)
input.grid(row=3, column=4)

second_button = Button(window, text="Click me more", command=button_clicked)
second_button.grid(row=0, column=3)

window.mainloop()