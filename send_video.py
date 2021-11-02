import socket
import pickle
import multiprocessing
import imutils
import cv2
import struct
import threading

host = "52.39.126.12"
port = 60001

conn = socket.socket()

conn.connect((host, port))
    
# send video
def send():
    while(True):

        vid = cv2.VideoCapture(0)
        while(vid.isOpened()):
            # metadata from the video frames (ex: pixel RGB values)
            img, frame = vid.read()
            frame = imutils.resize(frame, width=320)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            a = pickle.dumps(gray)
            message = struct.pack("Q", len(a)) + a

            # send frames from local webcam
            conn.sendall(message)

            cv2.imshow('Sending...', gray)
            key = cv2.waitKey(1)

send()


            