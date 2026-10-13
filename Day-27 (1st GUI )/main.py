import tkinter
from tkinter import *
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 1)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.minsize(250, 250)
window.title("convertor")
miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)

cal_button = Button(text="calculate",command=miles_to_km)
cal_button.grid(column=1, row=2)

window.mainloop()