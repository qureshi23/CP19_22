from tkinter import *
import socket
import sys
import time




s = socket.socket()
host = input(str("Please enter the host name of the server : "))
port=8080
s.connect((host,port))
print("Connected to chat server")
print("")

window = Tk()
window.title("Client Messenger")
window.geometry("440x150")

#Set Window's Background Color
window.configure(background='light grey')


title_label = Label(window,text="Client Messenger", bg="black", fg="white", font="comicsansms 12 bold", borderwidth=3)
title_label.grid(column=0,row=0)

text = Label(window,text="Text Message",font="comicsansms 12  ", bg="light grey", fg="black")
text.grid(column=0,row=1)

server_output_label = Label(window,text="Client Output", bg="light grey", fg="black",font="comicsansms 14 bold")
server_output_label.grid(column=0,row=3)

move = StringVar()
new = StringVar()


txt1 = Entry(window,width=30,textvariable=move,fg="blue")
txt1.grid(column=1,row=1)

txt2 = Entry(window, width=32,textvariable=new,state="disabled",fg="green")
txt2.grid(column=1, row=4)


    
    
#incoming_message = s.recv(1024)
#incoming_message = incoming_message.decode()
#new.set(incoming_message)
#print("Server : ",incoming_message)
#print("")




def msg():
    message = move.get()
    message = message.encode()
    s.send(message)
    print("Message has been sent...")
    print("")

btn = Button(window,text="Send",bg='blue',width=10,fg='white',font="comicsansms 10 bold ", command= msg)
btn.grid(column=1,row=2)

window.mainloop()