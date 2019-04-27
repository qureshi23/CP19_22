import socket
import sys
import time


s = socket.socket()
host = socket.gethostname()
print("server will start on host : ",host)
port = 4040
s.bind((host,port))
print("")
print("server connected to port successfully")
print("")
s.listen(1)
conn,addr = s.accept()
print(addr," Has connected to the server and is now online...")
print("")
