import cv2
import pickle
import struct
import socket
import imutils
import tty, sys, termios

# IP of the EC2 server
host = "52.39.126.12" 
port = 60000

payload_size = struct.calcsize("Q")

# make a video streaming socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    
    conn.connect((host, port))
    
    with conn:
        if conn:

            # OpenCV function, this will open the webcam on current machine
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

