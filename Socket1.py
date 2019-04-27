import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 50
client.connect((host, port))
data = client.recv(1024)
print(data)