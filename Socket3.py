import socket
server = socket.socket(socket.AF_STREAM, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 13))
server.listen(5)
while True:
    connection, address = server.accept()
    print('Got connection from', address)
    connection.send('Welcome to your server')
    connection.close()  # close the connection