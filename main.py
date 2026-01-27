from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=500)

#Labeles with Tkinter
my_label = Label(text="Label", font=("Arial", 25))
my_label.pack()

def button_clicked():
    print("clicked")
    my_label["text"] = "You pressed the button"

my_button = Button(text="Click Me", command=button_clicked)
my_button.pack()









window.mainloop()