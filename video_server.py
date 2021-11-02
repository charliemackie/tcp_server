import socket
import threading

host = '52.39.126.12'
port_commands = 60001

socketServer = socket.socket()

client = []

socketServer.bind((host, port_commands))
socketServer.listen(5)

def start(socketServer):
    while(True):
        conn, addr = socketServer.accept()
        client.append(conn)
        t = threading.Thread(target = send, args = (conn, ))
        t.start()

def send(fromConnection):
    try:
        while(True):
            data = fromConnection.recv(4096)
            for cl in client:
                if cl != fromConnection:
                    cl.send(data)
    except:
        print("Client Disconnected")

start(socketServer)




 