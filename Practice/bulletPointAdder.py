from tkinter import *
from time import *

def update():
    time = strftime("%I:%M:%S %p")
    time_label.config(text=time)
    date = strftime("%B %d, %Y")
    date_label.config(text=date)
    day = strftime("%A")
    day_label.config(text=day)
    time_label.after(1000, update)
window = Tk()

time_label = Label(window, fg="Orange", bg="Black", font="25")
time_label.pack()

day_label = Label(window, fg="Black")
day_label.pack()

date_label = Label(window, fg="Black")
date_label.pack()
year_label = Label(window, fg="Black")
year_label.pack()

update()



window.mainloop()