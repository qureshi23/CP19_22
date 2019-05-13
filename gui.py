###libaries grid form
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import Frame
from tkinter import *

###functions
def f1():
    print("button click")
    mb.showinfo("My Text","My Message")
def f2():
    print("button click")
    mb.showinfo("My Text",tv1.get())

##main code
#tv1 = StringVar()
root=tk.Tk()
form=Frame()
form.grid()
root.title("Chat Bot ")

tv1=StringVar()

l1=tk.Label(form,text="Inam Ali")
l1.grid(row=10,column=10)

#root. geometry("640x480")

b1=tk.Button(root,text="click",command=f1,fg="white", bg="black",height=10,width="10")
b1.grid(row=2,column=2,padx=10,pady=10)
b2=tk.Button(root,text="click",command=f2)
b2.grid(row=3,column=1,padx=10,pady=10)

# for text box

tb=tk.Entry(form,textvariable=tv1)
tb.grid(row=10,column=10)
#tb.grid(row=16,column=16)