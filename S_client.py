import socket
import sys
import time


s = socket.socket()
host = input(str("Please the host name of the server : "))
port=4040
s.connect((host,port))
print("Connected to server")
