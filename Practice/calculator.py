from tkinter import *


def button_press(num):
    global eq_text

    eq_text = eq_text + str(num)

    eq_var.set(eq_text)


def equals():
    global eq_text

    try:
        total = str(eval(eq_text))

        eq_var.set(total)
        eq_text = total
    except ZeroDivisionError:
        eq_text = ""

        eq_var.set("Arthmatic Error!")
    except SyntaxError:
        eq_text = ""

        eq_var.set("Syntax Error!")


def clear():
    global eq_text

    eq_text = ""

    eq_var.set("")


window = Tk()
window.title("Calculator")
window.geometry("500x500")

eq_text = ""

eq_var = StringVar()
label = Label(window, textvariable=eq_var, width=30, height=2, bg="white", font=("consolas", 20))
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, command=lambda: button_press(1))
button1.grid(row=0, column=0)
button2 = Button(frame, text=2, height=4, width=9, command=lambda: button_press(2))
button2.grid(row=0, column=1)
button3 = Button(frame, text=3, height=4, width=9, command=lambda: button_press(3))
button3.grid(row=0, column=2)
button4 = Button(frame, text=4, height=4, width=9, command=lambda: button_press(4))
button4.grid(row=2, column=0)
button5 = Button(frame, text=5, height=4, width=9, command=lambda: button_press(5))
button5.grid(row=2, column=1)
button6 = Button(frame, text=6, height=4, width=9, command=lambda: button_press(6))
button6.grid(row=2, column=2)
button7 = Button(frame, text=7, height=4, width=9, command=lambda: button_press(7))
button7.grid(row=3, column=0)
button8 = Button(frame, text=8, height=4, width=9, command=lambda: button_press(8))
button8.grid(row=3, column=1)
button9 = Button(frame, text=9, height=4, width=9, command=lambda: button_press(9))
button9.grid(row=3, column=2)
button0 = Button(frame, text=0, height=4, width=9, command=lambda: button_press(0))
button0.grid(row=4, column=0)
plus = Button(frame, text="+", height=4, width=9, command=lambda: button_press("+"))
plus.grid(row=0, column=3)
minus = Button(frame, text="-", height=4, width=9, command=lambda: button_press("-"))
minus.grid(row=2, column=3)
division = Button(frame, text="/", height=4, width=9, command=lambda: button_press("/"))
division.grid(row=3, column=3)
multiply = Button(frame, text="*", height=4, width=9, command=lambda: button_press("*"))
multiply.grid(row=4, column=3)
equal = Button(frame, text="=", height=4, width=9, command=lambda: equals())
equal.grid(row=4, column=2)
clear_all = Button(window, text="Clear", height=4, width=15, command=clear)
clear_all.pack()
window.mainloop()
