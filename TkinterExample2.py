from tkinter import *
 
window = Tk()
 
window.title("Welcome to Tkinter")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello Github")
 
lbl.grid(column=0, row=0)
 
btn = Button(window, text="Click Here")
 
btn.grid(column=1, row=0)
 
window.mainloop()