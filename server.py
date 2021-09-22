import socket

# open to any IP address
host = '0.0.0.0'
port = 60000

# make the socket and bind to incoming client connection
server = socket.socket()
server.bind((host, port))
server.listen(4)

clients = []

# accept connections
def start():
    while(True):
        conn, addr = server.accept()
        clients.append(conn)
        print(conn)
        while(True):
            data = conn.recv(4096)
            for c in clients:
                if c != conn:
                    c.sendall(data)
start()

