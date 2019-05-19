from tkinter import *
import socket
import sys
import time


s = socket.socket()
host = input(str("Please the host name of the server : "))
port=8080
s.connect((host,port))
print("Connected to chat server")

window = Tk()
window.title("Client Messenger")
window.geometry('350x200')
#lbl = Label(window, text="Hello")
#lbl.grid(column=0, row=0)
txt = Text(window,width=32,height=10)
txt.grid(column=1, row=0)
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Send", command=clicked)
btn.grid(column=2, row=0)
def message(self):
    incoming_message = self.s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server : ",incoming_message)
    print("")
    message = input(str(">>"))
    message = message.encode()
    self.s.send(message)
    print("Message has been sent...")
    print("")
        
window.mainloop()