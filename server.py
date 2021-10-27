import socket

host = '0.0.0.0'
port = 60000

# make the socket and bind to incoming client connection
server = socket.socket()
server.bind((host, port))
server.listen(4)

# accept connections
def start():
    while(True):
        conn1, add1 = server.accept()
        conn2, add2 = server.accept()
        print(conn1)
        print(conn2)
        while(conn1 != None and conn2 != None):
            data = conn1.recv(4096)
            data = conn2.recv(4096)
            conn1.sendall(data)
            conn2.sendall(data)
start()