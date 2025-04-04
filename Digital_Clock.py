from tkinter import Tk
from tkinter import Label
import time
import sys

root = Tk()
root.title("DigitalClock")


def present_time():
    display_time = time.strftime("%H:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200, present_time)

digi_clock = Label(root, font=("calibri", 40, "bold"), background="black", foreground="white")
digi_clock.pack(anchor="center")

present_time()
root.mainloop()
    