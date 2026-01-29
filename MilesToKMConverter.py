from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=200, height=200)

def calculate():
    miles_int = int(mile_input.get())
    km_int = miles_int * 1.60934
    km["text"] = km_int

mile_input = Entry(window, width=20, bd=3, text="0")
mile_input.grid(row=0, column=1)

equal_to = Label(window, text="Is Equal to:")
equal_to.grid(row=1, column=0)

km = Label(window, text="0")
km.grid(row=1, column=1)

km_text = Label(window, text="Km")
km_text.grid(row=1, column=2)

calculate_button = Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0)
calculate_button.grid(row=2, column=0)
calculate_button.grid(row=2, column=1)


window.mainloop()
