import tkinter as tk
from tkinter import messagebox as mb
from tkinter import Frame
from tkinter import *
def f1():
    print("Message Sent")
    mb.showinfo("Text","Message")
def f2():
    print("Message sent")
    mb.showinfo("ext",tv1.get())
root=tk.Tk()
form=Frame()
form.grid()
root.title("Chat app ")

tv1=StringVar()

l1=tk.Label(form,text="Yasir Ali")
l1.grid(row=10,column=10)
b1=tk.Button(root,text="Click here",command=f1,fg="white", bg="black",height=10,width="10")
b1.grid(row=2,column=2,padx=10,pady=10)
b2=tk.Button(root,text="SEND",command=f2)
b2.grid(row=3,column=1,padx=10,pady=10)
tb=tk.Entry(form,textvariable=tv1)
tb.grid(row=10,column=10)
root.mainloop()