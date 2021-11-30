import socket
import tty, sys, termios

host = "34.217.87.238"
port = 60000

conn = socket.socket()

conn.connect((host, port))

# send arrows       
def send():
    while(True):
        filedescriptors = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)
        x = 0
        while 1:
            x = sys.stdin.read(1)[0]
            encoded = bytes(x, 'utf-8')
            conn.sendall(encoded) 

send()
                              



                
                


