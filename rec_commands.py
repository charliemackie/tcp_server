import threading
import cv2
import socket
import pickle
import tty, sys, termios
import multiprocessing
import struct

host = "52.39.126.12"
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
                              



                
                


