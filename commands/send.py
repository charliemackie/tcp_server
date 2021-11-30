import socket

host = "34.217.87.238"
port = 60000

conn = socket.socket()

conn.connect((host, port))
    
# rec arrows
def rec():
    while(True):
        data = conn.recv(4096)
        message = data.decode('utf-8')

        if message == 'a':
            print("left")
        elif message == 'd':
            print("right")
        elif message == 's':
            print("down")
        elif message == 'w':
            print("up")

rec()   


            