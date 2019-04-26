import tkinter as tk
from tkinter import messagebox as mb
from tkinter import Frame

def f1():
    print("Button Click")
    mb.showinfo("My Text","Hello World")


root=tk.Tk()
form=Frame(root)
form.grid()
root.title("Chat Box")


b1=tk.Button(form,text="Click",command=f1)
b1.grid(row=3,column=1)


root.mainloop()
