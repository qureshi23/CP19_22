from tkinter import *
import socket
import sys
import time


s = socket.socket()
host = socket.gethostname()
print("server will start on host : ",host)
port = 8080
s.bind((host,port))
print("")
print("server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn,addr = s.accept()
print(addr," Has connected to the server and is now online...")
print("")

window = Tk()
window.title("Server Messenger")
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
    message = input(str(">>"))
    message = message.encode()
    conn.send(message)
    print("Message has been sent...")
    print("")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client : ",incoming_message)
    print("")

window.mainloop()