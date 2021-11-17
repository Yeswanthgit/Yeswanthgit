from tkinter import *
count = 0

window = Tk()
window.geometry("720x720")
window.title("Stranger Things")
#icon = PhotoImage(file="cat.png")
#window.iconphoto(True,icon)
window.config(background="#4AA999")


def call():
    global count
    print("Clicked!!!", count,"Times")
    count += 1


label = Label(window,text="YESWANTH",
              font=("RNS Sanz", 25, "bold"),
              fg="#00FF00",
              bg="black",
              relief=GROOVE,
              bd=10,
              padx=15,
              pady=10
              )
label.pack()

button = Button(window,
                text="Punch",
                fg="Red",
                bg="Green",
                activebackground="Green",
                activeforeground="Red",
                command=call,
                font=("RNS Sanz", 15)
                )

button.place(x=320, y=320)

#Button.pack(side=RIGHT)


def submit():

    username = entry.get()
    print("HELLO " + username)


entry = Entry(window,
            fg="Red",
            bg="Green",
            font=("RNS Sanz", 35),
            show="-"
            )
entry.pack(side=LEFT)
entry.place(x=120,y=220)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)
submit_button.place(x=220,y=280)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)
delete_button.place(x=270,y=280)

backspace_button = Button(window, text="BackSpace", command=backspace)
backspace_button.pack(side=RIGHT)
backspace_button.place(x=315,y=280)

window.mainloop()
