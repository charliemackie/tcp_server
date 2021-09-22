import socket
import threading 

# open to any IP address
host = '0.0.0.0'
port = 60000

# make the socket and bind to incoming client connection
server = socket.socket()
server.bind(host, port)
server.listen(4)

clients = []

# accept connections
def start():
    while(True):
        conn, addr = server.accept()
        clients.append(conn)
        # can multithread multiple connections
        t = threading.Thread(target = send, args = (conn, ))
        t.start()

# send the video data to all clients
def send(fromConnection):
    try:
        while(True):
            data = fromConnection.recv(4096)
            for c in clients:
                if c != fromConnection:
                    c.send(data)
    except:
        print("Client Disconnected")

start()

