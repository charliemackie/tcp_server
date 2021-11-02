import socket
import pickle
import multiprocessing
import imutils
import cv2
import struct
import threading

host = "52.39.126.12"
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


            