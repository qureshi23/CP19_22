from tkinter import *

window = Tk()

window.title("Welcome to Github")

window.geometry('350x200')

lbl = Label(window, text="Hello Subhan")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

def clicked():

    res = "Welcome to " + txt.get()

    lbl.configure(text= res)

btn = Button(window, text="Click Here", command=clicked)

btn.grid(column=3, row=1)

window.mainloop()