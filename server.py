import socket

host = '0.0.0.0'
port = 60000

# make the socket and bind to incoming client connection
server = socket.socket()
server.bind((host, port))
server.listen(2)

clients = []

# accept connections
def start():
    while(True):
        conn1, address1 = server.accept()
        conn2, address2 = server.accept()
        clients.append(conn1)
        clients.append(conn2)
        print(conn1)
        print(conn2)
        while(True & conn1 & conn2):
            data = conn1.recv(4096)
            conn2.sendall(data)
start()